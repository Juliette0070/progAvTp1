from django.db import models

# Create your models here.

class Product(models.Model):
    class Meta:
        verbose_name = "Produit"
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, null=True, blank=True, unique=True)
    prixHT = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True, verbose_name="Prix Unitaire HT")
    date_de_fabrication = models.DateField(default='2024-01-01', blank=True, verbose_name="Date création")
    statut = models.ForeignKey('Statut', on_delete=models.CASCADE, default=0)

    def __unicode__(self):
        return "{0} [{1}]".format(self.name, self.code)


class Productitem(models.Model):
    class Meta:
        verbose_name = "Déclinaison Produit"
    color = models.CharField(max_length=100)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    code = models.CharField(max_length=100, null=True, blank=True, unique=True)

    def __unicode__(self):
        return "{{0}} {1} [{{2}}]".format(self.product.name, self.color, self.product.code)

class Statut(models.Model):
    numero = models.IntegerField(default=0)
    libelle = models.CharField(max_length=100)

    def __unicode__(self):
        return "{0} [{1}]".format(self.libelle, self.numero)
