# Generated by Django 3.0.5 on 2021-07-28 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digitalpocket', '0017_auto_20210729_0143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadedfile',
            name='doc_id',
            field=models.AutoField(default='0', primary_key=True, serialize=False),
        ),
    ]