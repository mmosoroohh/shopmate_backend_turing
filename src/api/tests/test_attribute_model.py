from django.test import TestCase
from api.models import Attribute
from .factories.attribute import AttributeFactory


class AttributeModelTest(TestCase):
    """Test attribute model"""
    def setUp(self):
        """Initialize db"""
        self.data = {
            'attribute_id': 1,
            'name': 'Color'
        }

    def test_model_can_create_attribute(self):
        """Test attribute model can create"""
        attribute = AttributeFactory(name=self.data.get('name'))
        saved_attribute = Attribute.objects.get(name=self.data.get('name'))
        self.assertEqual(attribute, saved_attribute)
