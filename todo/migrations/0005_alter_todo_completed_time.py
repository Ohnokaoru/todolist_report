# Generated by Django 5.1 on 2024-09-02 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_alter_todo_completed_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='completed_time',
            field=models.DateTimeField(blank='', null=True),
        ),
    ]
