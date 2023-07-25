from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    # @property
    # def date(self):
    #     mydate = self.created
    #     return mydate.strftime("%m/%d/%Y, %H:%M:%S")
    #
    # @property
    # def bookscount(self):
    #     kitoblar = len(self.books.all())
    #     return kitoblar

    def __str__(self):
        return self.name
    class Meta:
        db_table = 'Categores'
        verbose_name = "Categore "
        verbose_name_plural = "Categores "


