# Generated by Django 2.0.1 on 2018-02-16 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='core/media', verbose_name='Imagem'),
        ),
    ]
