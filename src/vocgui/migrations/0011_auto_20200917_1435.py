# Generated by Django 3.1 on 2020-09-17 14:35

from django.db import migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('vocgui', '0010_auto_20200917_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='cropping',
            field=image_cropping.fields.ImageRatioField('image', '10x360', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='cropping'),
        ),
        migrations.AlterField(
            model_name='document',
            name='image',
            field=image_cropping.fields.ImageCropField(blank=True, upload_to='uploaded_images'),
        ),
    ]
