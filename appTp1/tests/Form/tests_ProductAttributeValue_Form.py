from django.test import TestCase
from appTp1.forms import ProductAttributeValueForm
from appTp1.models import ProductAttribute

class ProductAttributeValueFormTest(TestCase):
    def setUp(self):
        self.attribute = ProductAttribute.objects.create(name='Couleur')
    
    def test_form_valid_data(self):
        form = ProductAttributeValueForm(data={'value': 'Cyan', 'product_attribute': self.attribute.id, 'position': 1})
        self.assertTrue(form.is_valid())
    
    def test_form_invalid_data(self):
        form = ProductAttributeValueForm(data={'product_attribute': self.attribute.id, 'position': 1})
        self.assertFalse(form.is_valid())
        self.assertIn('value', form.errors)
    
    def test_form_invalid_product_attribute(self):
        form = ProductAttributeValueForm(data={'value': 'Cyan', 'position': 1})
        self.assertFalse(form.is_valid())
        self.assertIn('product_attribute', form.errors)
    
    def test_form_optional_position(self):
        form = ProductAttributeValueForm(data={'value': 'Vert', 'product_attribute': self.attribute.id, 'position': None})
        self.assertTrue(form.is_valid())
    
    def test_form_save(self):
        form = ProductAttributeValueForm(data={'value': 'Bleu', 'product_attribute': self.attribute.id, 'position': 2})
        self.assertTrue(form.is_valid())
        product_attribute_value = form.save()
        self.assertEqual(product_attribute_value.value, 'Bleu')
        self.assertEqual(product_attribute_value.product_attribute, self.attribute)
        self.assertEqual(product_attribute_value.position, 2)
