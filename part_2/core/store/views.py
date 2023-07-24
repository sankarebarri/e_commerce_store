from django.shortcuts import render, get_object_or_404

from .models import Category, Product


def product_all(request):
    
    # products = Product.objects.filter(is_active=True)
    # using a modelManagr() instead of filtering
    products = Product.products.all()
    context = {
        'products': products
    }
    return render(request, 'store/home.html', context)


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'store/products/single.html', {'product':product})


def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    context = {
        'category': category,
        'products': products
    }
    return render(request, 'store/products/category.html', context)