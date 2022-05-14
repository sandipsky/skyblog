# Generated by Django 3.2.9 on 2022-05-13 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('desc', models.TextField()),
                ('date_created', models.DateField(auto_now_add=True)),
                ('author', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
            ],
        ),
    ]
