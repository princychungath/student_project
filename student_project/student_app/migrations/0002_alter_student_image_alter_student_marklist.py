# Generated by Django 4.2.1 on 2023-06-22 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to='image'),
        ),
        migrations.AlterField(
            model_name='student',
            name='Marklist',
            field=models.FileField(blank=True, null=True, upload_to='marklist'),
        ),
    ]
