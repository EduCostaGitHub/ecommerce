# Generated by Django 5.0.6 on 2024-06-17 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_alter_product_promo_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='promo_price',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='producttype',
            name='promo_price',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
