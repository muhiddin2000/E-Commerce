from django.db import models
from django.utils.html import format_html

# Create your models here.
class Reklama(models.Model):
    name = models.CharField(max_length=600, help_text="Reklama nomini kiriting", verbose_name="Reklama nomi")
    image = models.ImageField(upload_to='reklama-images', help_text="Reklama rasmini yuklang",
                              verbose_name="Reklama rasmi")
    description = models.TextField(help_text="Reklama haqida kiriting", verbose_name="Reklama haqida qisqacha")
    viewed = models.IntegerField(help_text="Ko'rilganlari soni", verbose_name="Ko'rilganlari soni", null=True,
                                 blank=True)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'Reklama'
        verbose_name = "Reklama "
        verbose_name_plural = "Reklamalar "

    @property
    def image_show(self):
        return format_html('<img src={} width="50" height="50" style="border-radius:50%" />'.format(self.image.url))
