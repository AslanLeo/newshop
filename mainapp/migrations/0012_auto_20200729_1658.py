# Generated by Django 3.2.3 on 2021-05-21 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0011_auto_20200729_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(blank=True, null=True, related_name='related_cart', to='mainapp.CartProduct'),
        ),
    ]
