from django.db import models
from utils.images import resize_image


# Create your models here.
"""
Produto:
        Produto:
            nome - Char
            descricao_curta - Text
            descricao_longa - Text
            imagem - Image
            slug - Slug
            preco_marketing - Float
            preco_marketing_promocional - Float
            tipo - Choices
                ('V', 'Variável'),
                ('S', 'Simples'),
"""
class Product(models.Model):

    name = models.CharField(max_length=255)
    short_description = models.CharField(max_length=255)
    description= models.CharField(max_length=255)
    image = models.ImageField(upload_to='product_img/%Y/%m/', blank=True, null=True)
    slug = models.SlugField(unique=True)
    price = models.FloatField()
    promo_price = models.FloatField(default=0)
    p_type = models.CharField(
        default='V',
        max_length=1,
        choices=(
            ('V', 'variation'),
            ('S', 'Simple'),
        )
    )

    def save(self, *args, **kwargs) -> None:
        max_width = 800
        #before save
        current_image = str(self.image.name)

        #save
        supersave=super().save(*args, **kwargs)     
    
        #after saving
        file_changed = False

        if self.image:
            file_changed = current_image != self.image.name

        if file_changed:
            resize_image(self.image,max_width)

        return supersave


    def __str__(self) -> str:
        return self.name
        
"""

        Variacao:
            nome - char
            produto - FK Produto
            preco - Float
            preco_promocional - Float
            estoque - Int

"""
class ProductType(models.Model):
    name = models.CharField(max_length=55,  blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField()
    promo_price = models.FloatField(default=0)
    stock = models.PositiveIntegerField(default=1)

    def __str__(self) -> str:
        return self.name or self.product.name
    
    class Meta:
        verbose_name = 'Product Type'
        verbose_name_plural = 'Product Types'

