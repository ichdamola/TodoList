# Generated by Django 3.2.6 on 2021-08-14 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_alter_task_parent_tasks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='parent_tasks',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child_tasks', to='tasks.task'),
        ),
    ]