import factory
from factory.fuzzy import FuzzyText

from django.contrib.auth.models import User

from contact.models import Contact
from core.models import KeyValue
from post.models import Post, Tag


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


class KeyValueFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = KeyValue

    key = LazyFuzzyText()
    value = LazyFuzzyText()
    type = KeyValue.TYPES.setting


class ContactFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Contact

    source_name = LazyFuzzyText()
    contact_value = LazyFuzzyText()
