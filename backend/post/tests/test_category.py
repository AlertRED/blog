from random import randint
from uuid import UUID, uuid1
from factory.fuzzy import FuzzyText

from django.urls import reverse
from rest_framework import status

from blog import settings
from blog.factories import CategoryFactory, PostFactory, UserFactory
from blog.utils import BasicAPITestCase
from post.models import Category


class CategoryCreateTestCase(BasicAPITestCase):
    data = {
        'title': FuzzyText().fuzz(),
    }

    def _request(self, data: dict, is_auth: bool = True):
        if is_auth:
            self._auth(UserFactory())
        return self.client.post(
            reverse('api_category_create_list'),
            data=data,
        )

    def test_success_create_category(self):
        response = self._request(self.data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(Category.objects.all()), 1)

    def test_failure_create_category_with_long_title(self):
        response = self._request({})

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertFalse(len(Category.objects.all()))

    def test_failure_create_category_without_auth(self):
        response = self._request(self.data, is_auth=False)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertFalse(len(Category.objects.all()))


class CategoryGetListTestCase(BasicAPITestCase):

    def _request(self):
        return self.client.get(
            reverse('api_category_create_list'),
        )

    def test_success_get_list_category(self):
        count_categories = randint(5, settings.REST_FRAMEWORK['PAGE_SIZE'])
        for _ in range(count_categories):
            PostFactory(category=CategoryFactory())

        response = self._request()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()['results']), count_categories)
        self.assertEqual(len(Category.objects.all()), count_categories)


class CategoryGetTestCase(BasicAPITestCase):

    def _request(self, id: UUID):
        return self.client.get(
            reverse('api_category_get_put_patch_delete', args=[id]),
        )

    def test_success_get_category(self):
        data = {
            'title': FuzzyText().fuzz(),
        }
        category = CategoryFactory(**data)
        PostFactory(category=category)

        response = self._request(category.pk)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(Category.objects.all()), 1)
        self.assertEqual(len(Category.objects.filter(pk=category.pk)), 1)
        category: Category = Category.objects.filter(pk=category.pk)[0]
        self.assertEqual(category.title, data['title'])

    def test_failure_get_category_if_havent_posts_and_not_auth(self):
        data = {
            'title': FuzzyText().fuzz(),
        }
        category = CategoryFactory(**data)
        response = self._request(category.pk)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_success_get_category_if_havent_posts_and_auth(self):
        data = {
            'title': FuzzyText().fuzz(),
        }
        category = CategoryFactory(**data)
        self._auth(UserFactory())
        response = self._request(category.pk)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(Category.objects.all()), 1)
        self.assertEqual(len(Category.objects.filter(pk=category.pk)), 1)
        category: Category = Category.objects.filter(pk=category.pk)[0]
        self.assertEqual(category.title, data['title'])

    def test_failure_get_category_if_not_exist(self):
        response = self._request(uuid1())
        self.assertEqual(
            response.status_code,
            status.HTTP_404_NOT_FOUND,
        )


class CategoryUpdateTestCase(BasicAPITestCase):
    data = {
        'title': FuzzyText().fuzz(),
    }

    def _request(self, id: UUID, data: dict, is_auth: bool = True):
        if is_auth:
            self._auth(UserFactory())
        return self.client.put(
            reverse('api_category_get_put_patch_delete', args=[id]),
            data=data,
        )

    def test_success_update_category(self):
        category = CategoryFactory(**self.data)
        response = self._request(category.pk, self.data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        category: Category = Category.objects.filter(pk=category.pk)[0]
        self.assertEqual(category.title, self.data['title'])

    def test_failure_update_category_if_not_exist(self):
        response = self._request(1, self.data)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_failure_update_category_without_auth(self):
        category = CategoryFactory(**self.data)
        response = self._request(category.pk, self.data, is_auth=False)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        new_category: Category = Category.objects.filter(pk=category.pk)[0]
        self.assertEqual(new_category.title, category.title)


class CategoryDeleteTestCase(BasicAPITestCase):
    data = {
        'title': FuzzyText().fuzz(),
    }

    def _request(self, id: UUID, is_auth: bool = True):
        if is_auth:
            self._auth(UserFactory())
        return self.client.delete(
            reverse('api_category_get_put_patch_delete', args=[id]),
        )

    def test_success_delete_category(self):
        category = CategoryFactory(**self.data)
        response = self._request(category.pk)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(len(Category.objects.all()))

    def test_failure_delete_category_without_auth(self):
        category = CategoryFactory(**self.data)
        response = self._request(category.pk, is_auth=False)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(len(Category.objects.all()), 1)
