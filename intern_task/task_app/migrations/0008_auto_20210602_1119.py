# Generated by Django 3.1.2 on 2021-06-02 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_app', '0007_auto_20210602_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskupload',
            name='task_pic',
            field=models.FileField(blank=True, upload_to='task_app/static/task_app/images'),
        ),
    ]
