from django.test import TestCase
from appTp1.models import ProductAttribute, ProductAttributeValue

class ProductAttributeValueModelTest(TestCase):
    
    def setUp(self):
        self.attribute = ProductAttribute.objects.create(name='Couleur')
        self.value = ProductAttributeValue.objects.create(value='Vert', product_attribute=self.attribute, position=1)
    
    def test_product_attribute_value_creation(self):
        self.assertEqual(self.value.value, 'Vert')
        self.assertEqual(self.value.product_attribute.name, 'Couleur')
        self.assertEqual(self.value.position, 1)
    
    def test_string_representation(self):
        self.assertEqual(str(self.value), 'Vert [Couleur]')
    
    def test_update_product_attribute_value(self):
        self.value.value = 'Orange'
        self.value.save()
        updated_value = ProductAttributeValue.objects.get(id=self.value.id)
        self.assertEqual(updated_value.value, 'Orange')
    
    def test_delete_product_attribute_value(self):
        self.value.delete()
        self.assertEqual(ProductAttributeValue.objects.count(), 0)
