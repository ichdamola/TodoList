# Generated by Django 3.2.6 on 2021-08-14 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_auto_20210814_0830'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='parent_tasks',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.task'),
        ),
    ]
