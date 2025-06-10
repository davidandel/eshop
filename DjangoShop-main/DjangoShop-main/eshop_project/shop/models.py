from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Název kategorie')
    description = models.TextField(blank=True, verbose_name='Popis kategorie')

    class Meta:
        verbose_name = 'Kategorie'
        verbose_name_plural = 'Kategorie'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name='Kategorie')
    name = models.CharField(max_length=150, verbose_name='Název produktu')
    description = models.TextField(blank=True, verbose_name='Popis produktu')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Cena')
    stock = models.PositiveIntegerField(default=0, verbose_name='Skladová zásoba')
    image = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name='Obrázek produktu')

    class Meta:
        verbose_name = 'Produkt'
        verbose_name_plural = 'Produkty'

    def __str__(self):
        return self.name


class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Datum vytvoření')
    products = models.ManyToManyField(Product, through='OrderItem', verbose_name='Produkty v objednávce')

    class Meta:
        verbose_name = 'Objednávka'
        verbose_name_plural = 'Objednávky'

    def __str__(self):
        return f'Objednávka #{self.id} - {self.created_at.strftime("%Y-%m-%d %H:%M")}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Objednávka')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Produkt')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Množství')

    class Meta:
        verbose_name = 'Položka objednávky'
        verbose_name_plural = 'Položky objednávky'

    def __str__(self):
        return f'{self.quantity}x {self.product.name}'
