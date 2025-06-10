from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.home, name='home'),
    path('kategorie/', views.categories, name='categories'),
    path('kategorie/<int:pk>/', views.category_detail, name='category_detail'),
    path('produkty/', views.products, name='products'),
    path('produkt/<int:pk>/', views.product_detail, name='product_detail'),
    path('kontakt/', views.contact, name='contact'),
    # Košík
    path('kosik/', views.cart_view, name='cart'),
    path('pridat-do-kosiku/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('odebrat-z-kosiku/<int:pk>/', views.remove_from_cart, name='remove_from_cart'),
]
