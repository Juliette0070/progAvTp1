from django.test import SimpleTestCase, TestCase
from django.urls import reverse, resolve
from appTp1.models import ProductAttribute, ProductAttributeValue
from appTp1.views import ProductAttributeValueCreateView, ProductAttributeValueListView
from django.contrib.auth.models import User

class ProductAttributeValueTestUrls(SimpleTestCase):
    def test_create_view_url_is_resolved(self):
        url = reverse('value-add')
        self.assertEqual(resolve(url).func.view_class, ProductAttributeValueCreateView)
    
    def test_list_view_url_is_resolved(self):
        url = reverse('values')
        self.assertEqual(resolve(url).func.view_class, ProductAttributeValueListView)

class ProductAttributeValueTestUrlResponses(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='secret')
        self.client.login(username='testuser', password='secret')
    
    def test_create_view_status_code(self):
        response = self.client.get(reverse('value-add'))
        self.assertEqual(response.status_code, 200)
    
    def test_list_view_status_code(self):
        response = self.client.get(reverse('values'))
        self.assertEqual(response.status_code, 200)

class ProductAttributeValueTestUrlResponsesWithParameters(TestCase):
    def setUp(self):
        self.attribute = ProductAttribute.objects.create(name='Couleur')
        self.value = ProductAttributeValue.objects.create(product_attribute=self.attribute, value='Rouge')
    
    def test_detail_view_status_code(self):
        url = reverse('value-detail', args=[self.value.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_detail_view_status_code_invalid_id(self):
        url = reverse('value-detail', args=[9999])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

class ProductAttributeValueTestUrlRedirect(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='secret')
        self.client.login(username='testuser', password='secret')
        self.product_attribute = ProductAttribute.objects.create(name='Couleur')
    
    def test_redirect_after_creation(self):
        response = self.client.post(reverse('value-add'), {
            'value': 'Bleu',
            'product_attribute': self.product_attribute.id,
            'position': 2
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('/appTp1/value/1/'))
