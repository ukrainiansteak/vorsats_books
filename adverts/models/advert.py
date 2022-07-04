from django.core.validators import FileExtensionValidator
from django.db import models

from adverts.models.categories import Category


class Advert(models.Model):
    name = models.CharField("назва", max_length=200, null=False)
    author = models.CharField("автор", max_length=100, null=True, blank=True)
    category = models.IntegerField(verbose_name='категорія',
                                   choices=Category.choices,
                                   default=Category.OTHER)
    date_published = models.DateTimeField("дата публікації", auto_now_add=True)
    seller = models.ForeignKey(to='accounts.Profile', null=True,
                               on_delete=models.CASCADE,
                               related_name='seller_adverts',
                               verbose_name="продавець")
    buyer = models.ForeignKey(to='accounts.Profile',
                              on_delete=models.SET_NULL,
                              related_name='buyer_adverts',
                              verbose_name="покупець",
                              null=True, blank=True)
    description = models.TextField("опис", max_length=1000,
                                   blank=True, null=True)
    image = models.ImageField("фото", null=True, upload_to='pics/',
                              blank=True,
                              validators=[
                                  FileExtensionValidator(
                                      ['jpg', 'png', 'jpeg']
                                  )
                              ])
    price = models.DecimalField("ціна", max_digits=8, decimal_places=2, null=False)
    is_active = models.BooleanField("активне", default=True)

    class Meta:
        verbose_name_plural = 'оголошення'
        verbose_name = 'оголошення'
