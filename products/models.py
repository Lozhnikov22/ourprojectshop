from ckeditor.fields import RichTextField
from django.db import models
from category.models import Category


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    title = models.CharField(max_length=255)
    # decimal_places - цифры после зяпятой
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = RichTextField()
    quantity = models.PositiveIntegerField(default=0)
    available = models.BooleanField(default=False)
    image = models.ImageField(blank=True, null=True, upload_to='products')

    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)


    def __str__(self):
        return self.title