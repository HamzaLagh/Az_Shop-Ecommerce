from django.contrib import admin
from .models import Category, Product, Commande, Client

# Register your models here.
admin.site.site_header="Az_SHop"
admin.site.site_title="Az_Shop"
admin.site.index_title ="Admin"

class AdminCategorie(admin.ModelAdmin): 
    list_display = ('name','date_added')
    # list_editable = ('name',)
    
class AdminProduct(admin.ModelAdmin): 
    list_display = ('name','price','category','image','date_added')
    search_fields = ('name',)
    list_editable = ('price',)
    list_editable = ('image',)
    # list_editable = ('category',)
    
    
class AdminCommande(admin.ModelAdmin): 
    list_display = ('items','prenom','nom','email', 'mdps', 'adress', 'ville', 'total', 'date_commande')
    
class AdminClient(admin.ModelAdmin): 
    list_display = ('nom','prenom','email', 'mdps', 'adress', 'ville')
    
admin.site.register(Category,AdminCategorie)
admin.site.register(Product,AdminProduct)
admin.site.register(Commande, AdminCommande)
admin.site.register(Client, AdminClient)
