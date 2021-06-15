from django.contrib import admin

# Register your models here.
from comments.models import Feedback

admin.site.register(Feedback)
