# Generated by Django 5.0.6 on 2024-06-17 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_alter_product_promo_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producttype',
            name='promo_price',
            field=models.FloatField(blank=True, default=0),
        ),
    ]