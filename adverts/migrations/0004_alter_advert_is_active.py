# Generated by Django 4.0.6 on 2022-07-04 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adverts', '0003_alter_advert_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advert',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='активне'),
        ),
    ]