from django import views
from django.urls import path
from boutique.views import home,produit, panier,confirmation,jackets,header,profil_client,base,tshirt,contact,jeans,pantalonShorts,manteauxVestes,ensembles,pulls,chaussures,chemises
from .views import *

urlpatterns = [
    path('',home, name="home"),
    path('<int:myid>',produit, name="produit"),
    path('panier',panier, name="panier"),
    path('confirmation',confirmation, name="confirmation"),
    path('header',header, name="header"),
    path('jackets',jackets, name="jackets"),
    path('t-shirt',tshirt, name="t-shirt"),
    path('profil_client',profil_client, name="profil_client"),
    path('base',base, name="base"),
    path('contact',contact, name="contact"),
    path('jeans',jeans, name="jeans"),
    path('pantalons-shorts',pantalonShorts, name="pantalons-shorts"),
    path('manteaux-vestes',manteauxVestes, name="manteaux-vestes"),
    path('ensembles',ensembles, name="ensembles"),
    path('pulls',pulls, name="pulls"),
    path('chaussures',chaussures, name="chaussures"),
    path('chemises',chemises, name="chemises"),
]