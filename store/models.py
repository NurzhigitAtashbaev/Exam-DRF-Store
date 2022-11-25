from django.db import models


class Store(models.Model):
    title = models.CharField(max_length=155)
    description = models.TextField()
    product = models.ManyToManyField('Product')

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    price = models.IntegerField()
    count = models.IntegerField()

    def __str__(self):
        return self.title


class Buy(models.Model):
    shop = models.ManyToManyField(Store, )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Supply(models.Model):
    shop = models.OneToOneField(Store, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
