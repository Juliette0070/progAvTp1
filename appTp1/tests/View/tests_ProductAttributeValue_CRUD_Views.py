from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from appTp1.models import ProductAttribute, ProductAttributeValue


class ProductAttributeValueCreateTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='secret')
        self.client.login(username='testuser', password='secret')
        self.product_attribute = ProductAttribute.objects.create(name='Couleur')
    
    def test_create_view_get(self):
        response = self.client.get(reverse('value-add'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'appTp1/new_value.html')
    
    def test_create_view_post_valid(self):
        data = {
            'value': 'Violet',
            'product_attribute': self.product_attribute.id,
            'position': 1
        }
        response = self.client.post(reverse('value-add'), data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(ProductAttributeValue.objects.count(), 1)
        self.assertEqual(ProductAttributeValue.objects.first().value, 'Violet')

class ProductAttributeValueViewTest(TestCase):
    def setUp(self):
        self.product_attribute = ProductAttribute.objects.create(name='Couleur')
        self.product_attribute_value = ProductAttributeValue.objects.create(value='Violet', product_attribute=self.product_attribute, position=1)
    
    def test_detail_view(self):
        response = self.client.get(reverse('value-detail', args=[self.product_attribute_value.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'appTp1/detail_value.html')
        self.assertContains(response, 'Violet')
        self.assertContains(response, 'Couleur')

class ProductAttributeValueUpdateViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='secret')
        self.client.login(username='testuser', password='secret')
        self.product_attribute = ProductAttribute.objects.create(name="Couleur")
        self.product_attribute_value = ProductAttributeValue.objects.create(
        value='Violet', product_attribute=self.product_attribute, position=1)

    def test_update_view_get(self):
        response = self.client.get(reverse('value-update', args=[self.product_attribute_value.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'appTp1/update_value.html')

    def test_update_view_post_valid(self):
        data = { 'value': 'Jaune', 'product_attribute': self.product_attribute.id, 'position': 2 }
        response = self.client.post(reverse('value-update', 
        args=[self.product_attribute_value.id]), data)
        self.assertEqual(response.status_code, 302) 
        self.product_attribute_value.refresh_from_db() 
        self.assertEqual(self.product_attribute_value.value, 'Jaune') 
        self.assertEqual(self.product_attribute_value.position, 2)

class ProductAttributeValueDeleteViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='secret')
        self.client.login(username='testuser', password='secret')
        self.product_attribute = ProductAttribute.objects.create(name="Couleur")
        self.product_attribute_value = ProductAttributeValue.objects.create(
        value='Rouge', product_attribute=self.product_attribute, position=1)

    def test_delete_view_get(self):
        response = self.client.get(reverse('value-delete', args=[self.product_attribute_value.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'appTp1/delete_value.html')

    def test_delete_view_post(self):
        response = self.client.post(reverse('value-delete', args=[self.product_attribute_value.id]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(ProductAttributeValue.objects.count(), 0)

class ProductAttributeValueListViewTest(TestCase):
    def setUp(self):
        self.product_attribute = ProductAttribute.objects.create(name='Couleur')
        self.product_attribute_value = ProductAttributeValue.objects.create(value='Violet', product_attribute=self.product_attribute, position=1)
    
    def test_list_view(self):
        response = self.client.get(reverse('values'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'appTp1/list_values.html')
        self.assertContains(response, 'Violet')
        self.assertContains(response, 'Couleur')