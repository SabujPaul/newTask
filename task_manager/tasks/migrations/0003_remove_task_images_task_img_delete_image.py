# Generated by Django 5.0.1 on 2024-01-07 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_remove_task_img_image_task_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='images',
        ),
        migrations.AddField(
            model_name='task',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='pics'),
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]