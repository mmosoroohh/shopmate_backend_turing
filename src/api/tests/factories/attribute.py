import factory
from faker import Factory
from api.models import Attribute

faker = Factory.create()


class AttributeFactory(factory.DjangoModelFactory):
    # FACTORY_FOR = 'api.models.Attribute'
    # name = 'attribute'

    class Meta:
        model = Attribute

    name = faker.text()