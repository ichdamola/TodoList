# Generated by Django 3.2.6 on 2021-08-14 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_task_parent_tasks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='parent_tasks',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='tasks.task'),
        ),
    ]