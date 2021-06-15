from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150, default='SOME STRING')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        if not self.parent:
            return f"{self.name}"
        else:
            return f"{self.parent}--> {self.name}"

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'