# Generated by Django 3.1 on 2020-09-17 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vocgui', '0006_auto_20200825_1216'),
    ]

    operations = [
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'verbose_name': 'Bereich',
                'verbose_name_plural': 'Bereiche',
            },
        ),
    ]
