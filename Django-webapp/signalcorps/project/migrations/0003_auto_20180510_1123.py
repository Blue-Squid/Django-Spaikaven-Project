# Generated by Django 2.0.5 on 2018-05-10 05:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_communication_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='communication',
            name='id',
        ),
        migrations.AlterField(
            model_name='communication',
            name='c_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='communication',
            name='s_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.SignalCorps'),
        ),
    ]
