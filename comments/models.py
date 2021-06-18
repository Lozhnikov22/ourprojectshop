from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from account.models import CustomUser
from products.models import Product

User = get_user_model()

class Feedback(models.Model):
    author = models.ForeignKey(User, related_name='feedbacks', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='feedbacks', on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.author}-->{self.product}-->{self.created_at}-{self.body[0:10]}"
