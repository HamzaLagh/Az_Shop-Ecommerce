from django.db import models

# Create your models here.
class Category(models.Model):
    name= models.CharField(max_length=225)
    date_added = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-date_added']
    def __str__(self):
        return self.name
        
class Product(models.Model):
    name = models.CharField(max_length=225)
    price = models.FloatField()
    description = models.TextField()
    category = models.ForeignKey(Category, related_name='categorie', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static/images')
    date_added = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-date_added']
    def __str__(self):
        return self.name
    
class Commande(models.Model):
    items = models.CharField(max_length=300)
    total = models.CharField(max_length=225)
    nom = models.CharField(max_length=225)
    prenom = models.CharField(max_length=225)
    email = models.EmailField()
    mdps = models.CharField(max_length=225)
    adress = models.CharField(max_length=225)
    ville = models.CharField(max_length=225)
    date_commande = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_commande']
        
class Client(models.Model):
    nom = models.CharField(max_length=225)
    prenom = models.CharField(max_length=225)
    email = models.EmailField()
    mdps = models.CharField(max_length=225)
    adress = models.CharField(max_length=225)
    ville = models.CharField(max_length=225)
    date_inscription = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-date_inscription']
    