from django.shortcuts import render
from .models import Product

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406358270',
        'name': 'Carmella Geraldine Sutrisna',
        'class_name': 'PBP A',
        'products': Product.objects.all()
    }

    return render(request, "main.html", context)
