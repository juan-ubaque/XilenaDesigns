# Generated by Django 4.0.2 on 2023-11-24 01:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0004_cart_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='price',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='cart',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Products.product'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
    ]
