# Generated by Django 5.0.6 on 2024-06-14 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_alter_product_image_alter_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='product_img/%Y/%m/'),
        ),
    ]
