import factory

from .models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    tel = factory.Sequence(lambda n: f"{n:08d}")
    name = factory.Faker("name")
    is_active = True
