from random import randint
from factory.fuzzy import FuzzyText

from django.urls import reverse
from rest_framework import status

from blog.factories import TagFactory, UserFactory
from blog.utils import BasicAPITestCase
from post.models import Tag


class TagCreateTestCase(BasicAPITestCase):
    data = {
        'title': FuzzyText().fuzz(),
    }

    def _request(self, data: dict, is_auth: bool = True):
        if is_auth:
            self._auth(UserFactory())
        return self.client.post(
            reverse('api_tag_create_list'),
            data=data,
        )

    def test_success_create_tag(self):
        response = self._request(self.data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(Tag.objects.all()), 1)

    def test_failure_create_tag_with_long_title(self):
        response = self._request({})

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertFalse(len(Tag.objects.all()))

    def test_failure_create_tag_without_auth(self):
        response = self._request(self.data, is_auth=False)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertFalse(len(Tag.objects.all()))


class TagGetListTestCase(BasicAPITestCase):

    def _request(self):
        return self.client.get(
            reverse('api_tag_create_list'),
        )

    def test_success_get_list_tag(self):
        count_tags = randint(5, 10)
        for _ in range(count_tags):
            TagFactory()

        response = self._request()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(Tag.objects.all()), count_tags)


class TagGetTestCase(BasicAPITestCase):

    def _request(self, id: int):
        return self.client.get(
            reverse('api_tag_get_put_path_delete', args=[id]),
        )

    def test_success_get_tag(self):
        data = {
            'title': FuzzyText().fuzz(),
        }
        tag = TagFactory(**data)

        response = self._request(tag.pk)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(Tag.objects.all()), 1)
        self.assertEqual(len(Tag.objects.filter(pk=tag.pk)), 1)
        tag: Tag = Tag.objects.filter(pk=tag.pk)[0]
        self.assertEqual(tag.title, data['title'])

    def test_failure_get_tag_if_not_exist(self):
        response = self._request(1)
        self.assertEqual(
            response.status_code,
            status.HTTP_404_NOT_FOUND,
        )


class TagUpdateTestCase(BasicAPITestCase):
    data = {
        'title': FuzzyText().fuzz(),
    }

    def _request(self, id: int, data: dict, is_auth: bool = True):
        if is_auth:
            self._auth(UserFactory())
        return self.client.put(
            reverse('api_tag_get_put_path_delete', args=[id]),
            data=data,
        )

    def test_success_update_tag(self):
        tag = TagFactory(**self.data)
        response = self._request(tag.pk, self.data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        tag: Tag = Tag.objects.filter(pk=tag.pk)[0]
        self.assertEqual(tag.title, self.data['title'])

    def test_failure_get_tag_if_not_exist(self):
        response = self._request(1, self.data)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_failure_update_tag_without_auth(self):
        tag = TagFactory(**self.data)
        response = self._request(tag.pk, self.data, is_auth=False)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        new_tag: Tag = Tag.objects.filter(pk=tag.pk)[0]
        self.assertEqual(new_tag.title, tag.title)


class TagDeleteTestCase(BasicAPITestCase):
    data = {
        'title': FuzzyText().fuzz(),
    }

    def _request(self, id: int, is_auth: bool = True):
        if is_auth:
            self._auth(UserFactory())
        return self.client.delete(
            reverse('api_tag_get_put_path_delete', args=[id]),
        )

    def test_success_delete_tag(self):
        tag = TagFactory(**self.data)
        response = self._request(tag.pk)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(len(Tag.objects.all()))

    def test_failure_delete_tag_without_auth(self):
        tag = TagFactory(**self.data)
        response = self._request(tag.pk, is_auth=False)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(len(Tag.objects.all()), 1)
