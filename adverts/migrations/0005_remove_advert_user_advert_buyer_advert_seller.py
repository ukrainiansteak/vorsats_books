# Generated by Django 4.0.6 on 2022-07-04 14:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('adverts', '0004_alter_advert_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advert',
            name='user',
        ),
        migrations.AddField(
            model_name='advert',
            name='buyer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='buyer_adverts', to=settings.AUTH_USER_MODEL, verbose_name='покупець'),
        ),
        migrations.AddField(
            model_name='advert',
            name='seller',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='seller_adverts', to=settings.AUTH_USER_MODEL, verbose_name='продавець'),
            preserve_default=False,
        ),
    ]