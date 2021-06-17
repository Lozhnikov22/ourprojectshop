from django.db import models


class Category(models.Model):
    """>>> category_object.children.all()
<QuerySet [<Category: Спорт --> Футбол --> Лига чемпионов>]>
так работает related_name='children'"""
    name = models.CharField(max_length=150, default='SOME STRING')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, related_name='children', blank=True)
    """реопределяем метод str, если будет присутсвовать под категория то мы выводим 
    главную категорию + подкатегорию"""
    def __str__(self):
        if not self.parent:
            return f'{self.name}'
        else:
            return f'{self.parent} --> {self.name}'

    # Меняем имена в админке, для правильного отображения
    class Meta:
        verbose_name = 'category'  # пишет в единственном числе
        verbose_name_plural = 'categories'  # пишет во множественном числе

