from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Tariff(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    product = models.ForeignKey(Product, related_name='tariffs', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} ({self.price})'


class Promotion(models.Model):
    name = models.CharField(max_length=255)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
    tariffs = models.ManyToManyField(Tariff, related_name='promotions')

    def __str__(self):
        return self.name
