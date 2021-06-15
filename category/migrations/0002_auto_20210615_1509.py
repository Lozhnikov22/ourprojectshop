# Generated by Django 3.2.4 on 2021-06-15 09:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'category', 'verbose_name_plural': 'categoryes'},
        ),
        migrations.AddField(
            model_name='category',
            name='name',
            field=models.CharField(default='SOME STRING', max_length=150),
        ),
        migrations.AddField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='category.category'),
        ),
    ]
