# Generated by Django 3.1.2 on 2021-06-02 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_app', '0003_auto_20210602_1013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskupload',
            name='task_pic',
            field=models.FileField(upload_to='images'),
        ),
    ]
