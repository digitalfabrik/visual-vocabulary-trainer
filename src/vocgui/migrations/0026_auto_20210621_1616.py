# Generated by Django 3.2.2 on 2021-06-21 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vocgui', '0025_auto_20210621_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alternativeword',
            name='article',
            field=models.IntegerField(choices=[(0, 'keiner'), (1, 'der'), (2, 'die'), (3, 'das'), (4, 'die (Plural)')], default='', verbose_name='article'),
        ),
        migrations.AlterField(
            model_name='document',
            name='article',
            field=models.IntegerField(choices=[(0, 'keiner'), (1, 'der'), (2, 'die'), (3, 'das'), (4, 'die (Plural)')], default='', verbose_name='article'),
        ),
    ]