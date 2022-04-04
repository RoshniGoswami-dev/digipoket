# Generated by Django 3.0.5 on 2021-07-28 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digitalpocket', '0024_delete_uploadedfile'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedFile',
            fields=[
                ('docs_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(default='', max_length=10)),
                ('category', models.CharField(default='', max_length=30)),
                ('doc_title', models.CharField(default='', max_length=300)),
                ('doc_image', models.FileField(default='', upload_to='fields/images/uploaded')),
            ],
        ),
    ]
