from django.views import View
from django.http import (
    Http404, StreamingHttpResponse, HttpResponseForbidden,
)

class FileServerView(View):
    """ Скачать файл
    """

    chunk_size = 8192
    # mime_type_to_inline = (
    #     'application/pdf',
    # )

    def get(self, *_, filepath, **__):
        """ Скачать файл
        """
        try:
            expires = int(self.request.GET['Expires'])
            signature = self.request.GET['Signature']
        except (KeyError, ValueError):
            return HttpResponseForbidden()

        if not S3Boto3Storage.check_access(filepath, expires, signature):
            return HttpResponseForbidden()

        filename = os.path.basename(filepath)
        content_type = (
            MimeTypes().guess_type(filename)[0] or 'application/octet-stream'
        )

        try:
            with default_storage.open(filepath, 'rb') as storage_file:
                response = StreamingHttpResponse(
                    FileWrapper(storage_file, self.chunk_size),
                    content_type=content_type
                )
                response['Content-Length'] = storage_file.size
                response['X-Accel-Buffering'] = 'no'
                response["Content-Disposition"] = \
                    "{}; " \
                    "filename={ascii_filename};" \
                    "filename*=UTF-8''{utf_filename}".format(
                        'inline' if content_type in self.mime_type_to_inline else 'attachment',
                        ascii_filename=quote(filename),
                        utf_filename=quote(filename)
                    )
                return response
        except (FileNotFoundError, OSError) as exc:
            raise Http404 from exc