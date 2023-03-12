from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from .models import Product, Commande,Category,Client
from django.core.paginator import Paginator
from django.core.mail import send_mail


# Create your views here.
def home(request):
    product_object = Product.objects.all()
    catg = Category.objects.all()
    search_prod = request.GET.get('searchProd')
    if search_prod !='' and search_prod is not None:
        product_object = Product.objects.filter(name__icontains=search_prod)
    return render(request,'home.html',{'product_object': product_object})
def homeq(request):
    catg = Category.objects.all()
    return render(request,'home.html',{'catg': catg})

def produit(request,myid):
    product_object = Product.objects.get(id=myid)
    return render(request,'produit.html', {'Product': product_object})

def panier(request):
    if request.method=="POST":
        items= request.POST.get('items')
        total= request.POST.get('total')
        nom= request.POST.get('nom')
        prenom= request.POST.get('prenom')
        email= request.POST.get('email')
        mdps= request.POST.get('mdps')
        adress= request.POST.get('adress')
        ville= request.POST.get('ville')
        com = Commande(items=items,total=total, nom=nom, prenom=prenom, email=email, mdps=mdps, adress=adress, ville=ville)
        com.save()
        return redirect('confirmation')
    
    return render(request,'panier.html')

def confirmation(request):
    info = Commande.objects.all()[:1]
    for item in info:
        nom = item.nom
    return render(request,'confirmation.html',{'name':nom})

def jackets(request):
    
    post_by_category = Product.objects.filter(category=Category.objects.get(name="jean"))
    return render(request,'jackets.html',{'post_by_category': post_by_category})
    
def header(request):
    
    return render(request,'header.html')

def profil_client(request):
    client_object = Commande.objects.all()
   
    return render(request,'profil_client.html',{'client_object': client_object})


def base(request):
    
    return render(request,'base.html')

def tshirt(request):
    
    return render(request,'t-shirt.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('fullname')
        email = request.POST.get('email')
        objet = request.POST.get('objet')
        message = request.POST.get('message')
        
        data = {
            'name' : name,
            'email' : email,
            'objet' : objet,
            'message' : message
        }
        message = '''
        New message:{}
        
        From: {}
        '''.format(data['message'], data['email'])
        send_mail(data['objet'], message, '',['hlaghnimi4@gmail.com'])
    return render(request,'contact.html')
    
def jeans(request):
    
    return render(request,'jeans.html')

def pantalonShorts(request):
    
    return render(request,'pantalons-shorts.html')

def manteauxVestes(request):
    
    return render(request,'manteaux-vestes.html')

def ensembles(request):
    
    return render(request,'ensembles.html')

def pulls(request):
    
    return render(request,'pulls.html')

def chaussures(request):
    
    return render(request,'chaussures.html')

def chemises(request):
    
    return render(request,'chemises.html')

