# Generated by Django 3.2.6 on 2024-04-11 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Datas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.CharField(max_length=50)),
                ('market', models.CharField(max_length=50)),
                ('commodity', models.CharField(max_length=50)),
                ('variety', models.CharField(max_length=50)),
                ('grade', models.CharField(blank=True, max_length=50)),
                ('date', models.CharField(max_length=50)),
            ],
        ),
    ]
