from django.db import models


class CustomerCL(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class TagCL(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class ProductCL(models.Model):
    class Meta:
        verbose_name = "Гардероб"
        verbose_name_plural = "Гардеробы"

    name = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    discription = models.TextField()
    date_created = models.DateField(auto_now_add=True)
    tags = models.ManyToManyField(TagCL)

    def __str__(self):
        return self.name


class OrderCL(models.Model):
    STATUS = (
        ("Обробатывается", "Обробатывается"),
        ("На середине пути..", "На середине пути.."),
        ("Доставлен", "Доставлен"),
    )
    customer = models.ForeignKey(CustomerCL, on_delete=models.CASCADE)
    product = models.ForeignKey(
        ProductCL, on_delete=models.CASCADE, related_name="order_product"
    )
    date_created = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=200, choices=STATUS, default=True)

    def __str__(self):
        return self.product.name