import factory
import factory.fuzzy
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

from .models import CustomUser


class UsersFactory(factory.django.DjangoModelFactory):
    class Meta: 
        model = CustomUser
        
    username = factory.Faker('first_name')
    email = factory.LazyAttributeSequence(lambda o, n: '%s%d@.testsidesk.com' % (o.username, n))
    password = factory.LazyFunction(lambda: make_password('test'))

