# Generated by Django 3.2.12 on 2022-03-19 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursesrelease',
            name='image',
            field=models.ImageField(default=1, upload_to='courses_rel/', verbose_name='Картина'),
            preserve_default=False,
        ),
    ]
