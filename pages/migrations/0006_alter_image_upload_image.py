# Generated by Django 3.2.2 on 2021-05-18 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_alter_image_upload_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image_upload',
            name='image',
            field=models.ImageField(upload_to='uploads/'),
        ),
    ]
