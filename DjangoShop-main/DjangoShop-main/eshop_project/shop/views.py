from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product


def home(request):
    categories = Category.objects.all()
    products = Product.objects.filter(pk__isnull=False)[:8]  # jen produkty s platným pk
    return render(request, 'shop/home.html', {'categories': categories, 'products': products})

def categories(request):
    categories = Category.objects.all()
    return render(request, 'shop/categories.html', {'categories': categories})

def products(request):
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(name__icontains=query)
    else:
        products = Product.objects.all()
    return render(request, 'shop/products.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'shop/product_detail.html', {'product': product})

def contact(request):
    return render(request, 'shop/contact.html')




def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    products = Product.objects.filter(category=category)
    return render(request, 'shop/category_detail.html', {'category': category, 'products': products})

def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    cart = request.session.get('cart', {})
    cart[str(pk)] = cart.get(str(pk), 0) + 1
    request.session['cart'] = cart
    return redirect(request.META.get('HTTP_REFERER', 'shop:products'))

def remove_from_cart(request, pk):
    cart = request.session.get('cart', {})
    if str(pk) in cart:
        del cart[str(pk)]
        request.session['cart'] = cart
    return redirect('shop:cart')

def cart_view(request):
    cart = request.session.get('cart', {})
    products = []
    total = 0
    for pk, qty in cart.items():
        product = get_object_or_404(Product, pk=pk)
        products.append({'product': product, 'quantity': qty, 'subtotal': product.price * qty})
        total += product.price * qty
    return render(request, 'shop/cart.html', {'cart_products': products, 'total': total})
