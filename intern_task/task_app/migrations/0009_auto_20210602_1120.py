# Generated by Django 3.1.2 on 2021-06-02 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_app', '0008_auto_20210602_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskupload',
            name='task_description',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
    ]