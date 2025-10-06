from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.urls import reverse
from django.http import HttpResponseRedirect, JsonResponse

# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    context = {
        'last_login': request.COOKIES.get('last_login', 'Never'),
        'username': request.user.username,
    }
    return render(request, "main.html", context)


@login_required(login_url='/login')
def create_product(request):
    if request.method == "POST":
        name = request.POST.get("name")
        price = request.POST.get("price")
        description = request.POST.get("description")

        new_product = Product(
            name=name,
            price=price,
            description=description,
            user=request.user
        )
        new_product.save()

        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({
                "message": "Product created successfully",
                "product": {
                    "id": new_product.id,
                    "name": new_product.name,
                    "price": new_product.price,
                    "description": new_product.description,
                    "user": new_product.user.id,
                }
            })
        
        return redirect('main:show_main')

    return render(request, "create_product.html")


@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)
    context = {'product': product}
    return render(request, "product_detail.html", context)

def show_xml(request):
    product_list = Product.objects.all()
    xml_data = serializers.serialize("xml", product_list)
    return HttpResponse(xml_data, content_type="application/xml")

@login_required(login_url='/login') 
def show_json(request):
    product_list = Product.objects.all()
    view_filter = request.GET.get('view') 
    
    if view_filter == "my":
        product_list = Product.objects.filter(user=request.user)
    else:
        category_filter = request.GET.get('category')
        if category_filter:
            product_list = product_list.filter(category=category_filter)

    data = [
        {
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'user_id': product.user.id if product.user else None,
            'thumbnail': product.thumbnail,
            'brand': product.brand,
            'stock': product.stock
        }
        for product in product_list
    ]
    return JsonResponse(data, safe=False)

def show_xml_by_id(request, id):
   try:
       item = Product.objects.filter(pk= id)
       xml_data = serializers.serialize("xml", item)
       return HttpResponse(xml_data, content_type="application/xml")
   except Product.DoesNotExist:
       return HttpResponse(status=404)

def show_json_by_id(request, id):
    try:
        product = Product.objects.select_related('user').get(pk=id)
        data = {
            'id': str(product.id),
            'name': product.name,
            'description': product.description,
            'price': product.price,
            'user_id': product.user_id,
            'user_username': product.user.username if product.user_id else None,
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/login')
def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return JsonResponse({"message": "Product updated successfully"}, status=200)
        else:
            return JsonResponse({"error": "Invalid form data"}, status=400)
    else:
        form = ProductForm(instance=product)
    return render(request, "edit_product.html", {"form": form, "product": product})

@login_required(login_url='/login')
def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    if request.method in ["POST", "DELETE"]:  # POST fallback
        product.delete()
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({"message": "Product deleted successfully"}, status=200)
        else:
            return redirect('main:show_main')
    return JsonResponse({"error": "Invalid request"}, status=400)
