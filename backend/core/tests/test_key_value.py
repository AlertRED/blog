from random import randint
from uuid import UUID, uuid1
from factory.fuzzy import FuzzyText

from django.urls import reverse
from rest_framework import status

from blog import settings
from core.models import KeyValue
from blog.factories import KeyValueFactory, UserFactory
from blog.utils import BasicAPITestCase


class KeyValueCreateTestCase(BasicAPITestCase):
    def setUp(self) -> None:
        self.data = {
            'key': FuzzyText().fuzz(),
            'value': FuzzyText().fuzz(),
            'type': KeyValue.TYPES.setting,
        }

    def _request(self, data: dict, is_auth: bool = True):
        if is_auth:
            self._auth(UserFactory())
        return self.client.post(
            reverse('api_key_value_create_list'),
            data=data,
        )

    def test_success_create_key_value(self):
        response = self._request(self.data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(KeyValue.objects.all()), 1)

    def test_failure_create_key_value_without_auth(self):
        response = self._request(self.data, is_auth=False)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertFalse(len(KeyValue.objects.all()))

    def test_failure_create_key_value_without_key(self):
        data = {
            'value': FuzzyText().fuzz(),
            'type': KeyValue.TYPES.setting,
        }
        response = self._request(data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertFalse(len(KeyValue.objects.all()))

    def test_failure_create_key_value_without_value(self):
        data = {
            'key': FuzzyText().fuzz(),
            'type': KeyValue.TYPES.setting,
        }
        response = self._request(data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertFalse(len(KeyValue.objects.all()))

    def test_failure_create_key_value_without_type(self):
        data = {
            'key': FuzzyText().fuzz(),
            'value': FuzzyText().fuzz(),
        }
        response = self._request(data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertFalse(len(KeyValue.objects.all()))


class KeyValueGetListTestCase(BasicAPITestCase):

    def _request(self, is_auth: bool = True):
        if is_auth:
            self._auth(UserFactory())
        return self.client.get(
            reverse('api_key_value_create_list'),
        )

    def test_success_get_list_key_value(self):
        count_key_values = randint(5, settings.REST_FRAMEWORK['PAGE_SIZE'])
        for _ in range(count_key_values):
            KeyValueFactory()

        response = self._request()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()['results']), count_key_values)
        self.assertEqual(len(KeyValue.objects.all()), count_key_values)


class KeyValueGetTestCase(BasicAPITestCase):

    def setUp(self) -> None:
        self.data = {
            'key': FuzzyText().fuzz(),
            'value': FuzzyText().fuzz(),
            'type': KeyValue.TYPES.setting,
        }

    def _request(self, id: UUID):
        return self.client.get(
            reverse('api_key_value_get_put_patch_delete', args=[id]),
        )

    def test_success_get_key_value(self):
        key_value = KeyValueFactory(**self.data)

        response = self._request(key_value.pk)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(KeyValue.objects.all()), 1)
        self.assertEqual(len(KeyValue.objects.filter(pk=key_value.pk)), 1)
        key_value: KeyValue = KeyValue.objects.filter(pk=key_value.pk)[0]
        self.assertEqual(key_value.key, self.data['key'])

    def test_failure_get_key_value_if_not_exist(self):
        response = self._request(uuid1())
        self.assertEqual(
            response.status_code,
            status.HTTP_404_NOT_FOUND,
        )


class KeyValueUpdateTestCase(BasicAPITestCase):

    def setUp(self) -> None:
        self.data = {
            'key': FuzzyText().fuzz(),
            'value': FuzzyText().fuzz(),
            'type': KeyValue.TYPES.setting,
        }

    def _request(self, id: UUID, data: dict, is_auth: bool = True):
        if is_auth:
            self._auth(UserFactory())
        return self.client.put(
            reverse('api_key_value_get_put_patch_delete', args=[id]),
            data=data,
        )

    def test_success_update_key_value(self):
        key_value = KeyValueFactory()
        response = self._request(key_value.pk, self.data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        key_value: KeyValue = KeyValue.objects.filter(pk=key_value.pk)[0]
        self.assertEqual(key_value.key, self.data['key'])

    def test_failure_update_key_value_if_not_exist(self):
        response = self._request(1, self.data)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_failure_update_key_value_without_auth(self):
        key_value = KeyValueFactory(**self.data)
        response = self._request(key_value.pk, self.data, is_auth=False)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        new_key_value: KeyValue = KeyValue.objects.filter(pk=key_value.pk)[0]
        self.assertEqual(new_key_value.key, key_value.key)


class KeyValueDeleteTestCase(BasicAPITestCase):
    def setUp(self) -> None:
        self.data = {
            'key': FuzzyText().fuzz(),
            'value': FuzzyText().fuzz(),
            'type': KeyValue.TYPES.setting,
        }

    def _request(self, id: UUID, is_auth: bool = True):
        if is_auth:
            self._auth(UserFactory())
        return self.client.delete(
            reverse('api_key_value_get_put_patch_delete', args=[id]),
        )

    def test_success_delete_key_value(self):
        key_value = KeyValueFactory(**self.data)
        response = self._request(key_value.pk)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(len(KeyValue.objects.all()))

    def test_failure_delete_key_value_without_auth(self):
        key_value = KeyValueFactory(**self.data)
        response = self._request(key_value.pk, is_auth=False)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(len(KeyValue.objects.all()), 1)
