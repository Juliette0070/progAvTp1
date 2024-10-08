
from django.db import models
from django.utils import timezone

PRODUCT_STATUS = (
    (0, 'Offline'),
    (1, 'Online'),
    (2, 'Out of stock')              
)

ORDER_STATUS = (
    (0, 'En Préparation'),
    (1, 'Passée'),
    (2, 'Reçue'),
)


"""
Produit : nom, code, etc.
"""
class Product(models.Model):

    class Meta:
        verbose_name = "Produit"

    name          = models.CharField(max_length=100)
    code          = models.CharField(max_length=10, null=True, blank=True, unique=True)
    price_ht      = models.DecimalField(max_digits=8, decimal_places=2,  null=True, blank=True, verbose_name="Prix unitaire HT")
    price_ttc     = models.DecimalField(max_digits=8, decimal_places=2,  null=True, blank=True, verbose_name="Prix unitaire TTC")
    status        = models.SmallIntegerField(choices=PRODUCT_STATUS, default=0)
    date_creation = models.DateTimeField(blank=True, verbose_name="Date création", default=timezone.now) 
    stock         = models.IntegerField(default=0)

    def __str__(self):
        return "{0} {1}".format(self.name, self.code)



class Fournisseur(models.Model):
    """
    Fournisseur de produit
    """
    
    class Meta:
        verbose_name = "Fournisseur"
        
    name               = models.CharField(max_length=100)


    def __str__(self):
        return "{0}".format(self.name)
    

class Commande(models.Model):
    """
    Commande de produit
    """
    
    class Meta:
        verbose_name = "Commande"
        
    date_commande       = models.DateTimeField("Date commande", default=timezone.now)
    product_fournisseur = models.ForeignKey('ProductFournisseur', on_delete=models.CASCADE)
    quantity            = models.IntegerField(default=0)
    etat                = models.SmallIntegerField(choices=ORDER_STATUS, default=0)

    def __str__(self):
        return "{0} {1}".format(self.quantity, self.product_fournisseur)
    

class ProductFournisseur(models.Model):
    """
    Produit fourni par un fournisseur
    """
    
    class Meta:
        verbose_name = "Produit Fournisseur"
        
    product            = models.ForeignKey('Product', on_delete=models.CASCADE)
    fournisseur        = models.ForeignKey('Fournisseur', on_delete=models.CASCADE)
    prix               = models.DecimalField(max_digits=8, decimal_places=2,  null=True, blank=True, verbose_name="Prix")

    def __str__(self):
        return "{0}: {1} ({2}€)".format(self.fournisseur, self.product.name, self.prix)
    


# Inutile pour le TP noté

"""
    Status : numero, libelle
"""
class Status(models.Model):
    numero  = models.IntegerField()
    libelle = models.CharField(max_length=100)
          
    def __str__(self):
        return "{0} {1}".format(self.numero, self.libelle)
    


"""
    Déclinaison de produit déterminée par des attributs comme la couleur, etc.
"""
class ProductItem(models.Model):
    
    class Meta:
        verbose_name = "Déclinaison Produit"

    code    = models.CharField(max_length=10, null=True, blank=True, unique=True)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    attributes  = models.ManyToManyField("ProductAttributeValue", related_name="product_item", blank=True)
       
    def __str__(self):
        return "{0}".format(self.code)
    

class ProductAttribute(models.Model):
    """
    Attributs produit
    """
    
    class Meta:
        verbose_name = "Attribut"
        
    name =  models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class ProductAttributeValue(models.Model):
    """
    Valeurs des attributs
    """
    
    class Meta:
        verbose_name = "Valeur attribut"
        ordering = ['position']
        
    value              = models.CharField(max_length=100)
    product_attribute  = models.ForeignKey('ProductAttribute', verbose_name="Unité", on_delete=models.CASCADE)
    position           = models.PositiveSmallIntegerField("Position", null=True, blank=True)
     
    def __str__(self):
        return "{0} [{1}]".format(self.value, self.product_attribute)
