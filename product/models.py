from django.db import models

# Create your models here.
from category.models import Category
from django.utils.html import format_html


class Product(models.Model):
    name = models.CharField(max_length=600, help_text="Mahsulot nomini kiriting", verbose_name="Mahsulot nomi")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, help_text="Mahsulot kategoriyasini tanlang",
                                 verbose_name="Mahsulot kategoriyasi")
    image = models.ImageField(upload_to='product-images', help_text="Mahsulot rasmini yuklang",
                              verbose_name="Mahsulot rasmi")
    description = models.TextField(help_text="Mahsulot haqida kiriting", verbose_name="Mahsulot haqida qisqacha")
    cost = models.IntegerField(help_text="Mahsulot narxini kiriting", verbose_name="Mahsulot narxi")
    discount = models.IntegerField(help_text="Mahsulot chegirma narxini kiriting", verbose_name="Chegirma narxi",
                                   default=0)
    viewed = models.IntegerField(help_text="Ko'rilganlari soni", verbose_name="Ko'rilganlari soni", null=True,
                                 blank=True)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Products'
        verbose_name = "Mahsulot "
        verbose_name_plural = "Mahsulotlar "

    @property
    def image_show(self):
        return format_html('<img src={} width="50" height="50" style="border-radius:50%" />'.format(self.image.url))
