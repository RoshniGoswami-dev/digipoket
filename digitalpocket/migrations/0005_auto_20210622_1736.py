# Generated by Django 3.0.5 on 2021-06-22 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digitalpocket', '0004_fieldview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fieldview',
            name='field_image',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]
