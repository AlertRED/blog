from random import randint
from factory.fuzzy import FuzzyText

from django.urls import reverse
from rest_framework import status

from contact.models import Contact
from blog.factories import ContactFactory, UserFactory
from blog.utils import BasicAPITestCase


class ContactCreateTestCase(BasicAPITestCase):
    data = {
        'source_name': FuzzyText().fuzz(),
        'contact_value': FuzzyText().fuzz(),
    }

    def _request(self, data: dict, is_auth: bool = True):
        if is_auth:
            self._auth(UserFactory())
        return self.client.post(
            reverse('api_contact_create_list'),
            data=data,
        )

    def test_success_create_key_value(self):
        response = self._request(self.data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(Contact.objects.all()), 1)

    def test_failure_create_contact_without_auth(self):
        response = self._request(self.data, is_auth=False)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertFalse(len(Contact.objects.all()))

    def test_failure_create_contact_without_contact_value(self):
        data = {
            'contact_value': FuzzyText().fuzz(),
        }
        response = self._request(data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertFalse(len(Contact.objects.all()))

    def test_failure_create_contact_without_contact_value(self):
        data = {
            'source_name': FuzzyText().fuzz(),
        }
        response = self._request(data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertFalse(len(Contact.objects.all()))

    def test_failure_create_contact_without_type(self):
        data = {
            'key': FuzzyText().fuzz(),
            'value': FuzzyText().fuzz(),
        }
        response = self._request(data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertFalse(len(Contact.objects.all()))


class ContactGetListTestCase(BasicAPITestCase):

    def _request(self, is_auth: bool = True):
        return self.client.get(
            reverse('api_contact_create_list'),
        )

    def test_success_get_list_key_value(self):
        count_key_values = randint(5, 10)
        for _ in range(count_key_values):
            ContactFactory()

        response = self._request()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), count_key_values)


class ContactGetTestCase(BasicAPITestCase):

    data = {
        'source_name': FuzzyText().fuzz(),
        'contact_value': FuzzyText().fuzz(),
    }

    def _request(self, id: int):
        return self.client.get(
            reverse('api_contact_get_put_patch_delete', args=[id]),
        )

    def test_success_get_key_value(self):
        key_value = ContactFactory(**self.data)

        response = self._request(key_value.pk)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(Contact.objects.all()), 1)
        self.assertEqual(len(Contact.objects.filter(pk=key_value.pk)), 1)
        key_value: Contact = Contact.objects.filter(pk=key_value.pk)[0]
        self.assertEqual(key_value.source_name, self.data['source_name'])

    def test_failure_get_contact_if_not_exist(self):
        response = self._request(1)
        self.assertEqual(
            response.status_code,
            status.HTTP_404_NOT_FOUND,
        )


class ContactUpdateTestCase(BasicAPITestCase):
    data = {
        'source_name': FuzzyText().fuzz(),
        'contact_value': FuzzyText().fuzz(),
    }

    def _request(self, id: int, data: dict, is_auth: bool = True):
        if is_auth:
            self._auth(UserFactory())
        return self.client.put(
            reverse('api_contact_get_put_patch_delete', args=[id]),
            data=data,
        )

    def test_success_update_key_value(self):
        key_value = ContactFactory(**self.data)
        response = self._request(key_value.pk, self.data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        key_value: Contact = Contact.objects.filter(pk=key_value.pk)[0]
        self.assertEqual(key_value.source_name, self.data['source_name'])

    def test_failure_update_contact_if_not_exist(self):
        response = self._request(1, self.data)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_failure_update_contact_without_auth(self):
        key_value = ContactFactory(**self.data)
        response = self._request(key_value.pk, self.data, is_auth=False)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        new_key_value: Contact = Contact.objects.filter(pk=key_value.pk)[0]
        self.assertEqual(new_key_value.source_name, key_value.source_name)


class ContactDeleteTestCase(BasicAPITestCase):
    data = {
        'source_name': FuzzyText().fuzz(),
        'contact_value': FuzzyText().fuzz(),
    }

    def _request(self, id: int, is_auth: bool = True):
        if is_auth:
            self._auth(UserFactory())
        return self.client.delete(
            reverse('api_contact_get_put_patch_delete', args=[id]),
        )

    def test_success_delete_key_value(self):
        key_value = ContactFactory(**self.data)
        response = self._request(key_value.pk)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(len(Contact.objects.all()))

    def test_failure_delete_contact_without_auth(self):
        key_value = ContactFactory(**self.data)
        response = self._request(key_value.pk, is_auth=False)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(len(Contact.objects.all()), 1)
