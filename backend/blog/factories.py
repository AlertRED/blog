import factory
from factory.fuzzy import FuzzyText

from django.contrib.auth.models import User

from posts.models import Post, Tag


def LazyFuzzyText(**data):
    return factory.LazyFunction(lambda: FuzzyText(**data).fuzz())


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = LazyFuzzyText()
    password = LazyFuzzyText()


class TagFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Tag

    title = LazyFuzzyText()


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = LazyFuzzyText()
    body = LazyFuzzyText()
