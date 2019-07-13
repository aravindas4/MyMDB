import factory

from faker import Faker

from apps.user import models

fake = Faker()


class UserFactory(factory.django.DjangoModelFactory):
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.LazyAttribute(
        lambda obj:
        f'{obj.first_name.lower()}_{obj.last_name.lower()}@example.com')
    username = factory.LazyAttribute(lambda obj: obj.email)

    class Meta:
        model = models.User
