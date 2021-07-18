# Generated by Django 3.2.2 on 2021-07-18 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vocgui', '0027_merge_20210622_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='word_type',
            field=models.CharField(choices=[('Nomen', 'Substantiv'), ('Verb', 'Verb'), ('Adjektiv', 'Adjektiv')], default='', max_length=255, verbose_name='word type'),
        ),
    ]
