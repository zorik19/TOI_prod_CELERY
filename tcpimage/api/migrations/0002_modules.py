# Generated by Django 3.0.2 on 2021-09-09 08:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Modules',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_module', models.CharField(max_length=100)),
                ('module_broken', models.CharField(max_length=100)),
                ('red_module', models.CharField(max_length=10000)),
                ('green_module', models.CharField(max_length=10000)),
                ('blue_module', models.CharField(max_length=10000)),
                ('cabinet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modules', to='api.Cabinets')),
            ],
            options={
                'ordering': ['item_module'],
            },
        ),
    ]
