from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .forms import ProductForm, RawProductForm

from .models import Product

# def product_create_view(request) : 
#     my_form = RawProductForm(request.GET) 
#     if request.method == "POST" : 
#         my_form = RawProductForm(request.POST) 
#         if my_form.is_valid() : 
#             # now the data is good 
#             print(my_form.cleaned_data)
#             Product.objects.create(**my_form.cleaned_data)

#         else : 
#             print(my_form.errors)
#     context = { 
#         "form" : my_form 
#     }
#     return render(request, "product_create.html", context)



# def product_create_view(request) : 
#     print(request.GET)
#     print(request.POST)
#     title = request.POST.get('title')
#     context = {
        
#     }
#     return render(request, "product_create.html", context)


def product_create_view(request) : 
    form = ProductForm(request.POST or None) 
    if form.is_valid(): 
        form.save() 
        form = ProductForm()

    context = {
        "form"  : form 
    }
    return render(request, "product_create.html", context) 



# Create your views here.
def product_detail_view(request) : 
    obj = Product.objects.get(id = 1)
    context = {
        "title" : obj.title,
        "description": obj.description

    }
    return render(request, "product/detail.html", {})

def render_initial_data(request):
    initial_data = { 
        'title' : "My this awesome title"
    }
    obj = Product.objects.get(id= 1)
    form = RawProductForm(request.POST or None ) # instance = obj) 
    if form.is_valid(): 
        form.save()
    context = { 
        'form' : form
    }
    return render(request, "product_create.html",context)

def dynamic_lookup_view(request, my_id) : 
    #obj =Product.objects.get(id = my_id )
    obj = get_object_or_404(Product, id = my_id)   # this is the fastest to catch 404
    #try:
    #    obj = Product.objects.get(id = my_id) 
    #except Product.DoesNotExist:
    #    raise Http404 
    if request.method == "POST":
        #confirming delete
        obj.delete() 
    context = { 
        "object" : obj,  
    }
    return render(request, "product_create.html",context)

def product_list_view(request) : 
    queryset= Product.objects.all() 
    context = { 
        "object_list"  : queryset 
    }
    return render(request, "product_create.html",context) 