from django.contrib.auth import get_user_model
from django.db import models
from django.http import HttpResponse

from products.models import Product

User = get_user_model()


class CartManger(models.Manager):
    def get_or_new(self, request):
        user = request.user  # вытаскиваем юзера который делает запрос
        cart_id = request.session.get('cart_id', None)
        if user is not None and user.is_authenticated:
            try:
                if user.cart:
                    cart_obj = request.user.cart  # выводит корзину нашего user, если он зареган

                else:
                    cart_obj = Cart.objects.get(pk=cart_id)
                    cart_obj.user = user
                    cart_obj.save()  # добавляет объект в корзину
                return cart_obj
            except:
                 HttpResponse("Ваша корзина пуста!")
        else:
            cart_obj = Cart.objects.get_or_create(pk=cart_id)
            cart_id = request.session['cart_id'] = cart_obj[0].id
            return cart_obj[0]


class Cart(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    objects = CartManger()

    def __str__(self):
        return f"cart for {self.user}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')
    product_item = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_in_cart')
    amount = models.PositiveIntegerField(default=1, blank=True)

    def __str__(self):
        return f"{self.cart.id} == cart item"
