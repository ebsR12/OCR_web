# Generated by Django 2.1.7 on 2019-02-18 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('internal_reference', models.CharField(max_length=100, unique=True, verbose_name='Internal Reference')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('image', models.ImageField(upload_to='OCR_image/input/', verbose_name='Input Image')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Create at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Update at')),
            ],
            options={
                'verbose_name': 'ImageFile',
                'verbose_name_plural': 'ImageFiles',
                'ordering': ['id'],
            },
        ),
    ]
