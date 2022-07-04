from django.core.validators import FileExtensionValidator
from django.db import models


class Advert(models.Model):
    name = models.CharField("назва", max_length=200, null=False)
    author = models.CharField("автор", max_length=100, null=True, blank=True)
    date_published = models.DateTimeField("дата публікації", auto_now_add=True)
    user = models.ForeignKey(to='accounts.Profile', on_delete=models.CASCADE,
                             related_name='adverts', verbose_name="користувач")
    description = models.TextField("опис", max_length=1000)
    image = models.ImageField(
        "фото",
        null=True,
        upload_to='pics/',
        blank=True,
        validators=[
            FileExtensionValidator(['jpg', 'png', 'jpeg'])
        ]
    )
    price = models.DecimalField("ціна", max_digits=8, decimal_places=2, null=False)
    is_active = models.BooleanField("активне", default=True)

    class Meta:
        verbose_name_plural = 'оголошення'
        verbose_name = 'оголошення'
