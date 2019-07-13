import factory.fuzzy

from django.utils.text import slugify
from faker import Faker

from apps.movie import models
from apps.user.factory import UserFactory

fake = Faker()


class MovieFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = models.Movie

    title = factory.Faker('title')
    plot = factory.Faker('paragraph')
    date = fake.past_datetime(start_date="-120y", tzinfo=None).date()
    runtime = factory.fuzzy.FuzzyChoice([90, 150])
    website = factory.LazyAttribute(
        lambda obj: f'https://www.{slugify(obj.title)}.com')
    rating = factory.fuzzy.FuzzyChoice([x[0] for x in models.Movie.RATING_TYPE])


class MovieImageFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = models.MovieImage

    user = factory.SubFactory(MovieFactory)
    movie = factory.SubFactory(UserFactory)
    path = factory.Faker('unix_device')


class PersonFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = models.Person

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    date_of_birth = fake.past_datetime(start_date="-20y", tzinfo=None).date()


class MoviePersonFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = models.MoviePerson

    movie = factory.SubFactory(MovieFactory)
    person = factory.SubFactory(PersonFactory)
    role = factory.fuzzy.FuzzyChoice([x[0] for x in models.MoviePerson.ROLE])


class VoteFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = models.Vote

    movie = factory.SubFactory(MovieFactory)
    user = factory.SubFactory(UserFactory)
    vote = factory.fuzzy.FuzzyChoice([x[0] for x in models.Vote.VOTE_TYPE])
