# Generated by Django 4.1.5 on 2023-02-28 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dress',
            fields=[
                ('custom_dress_id', models.IntegerField(primary_key=True, serialize=False)),
                ('custom_size', models.CharField(max_length=10)),
                ('custom_fabric', models.CharField(max_length=20)),
                ('custom_colour', models.CharField(max_length=20)),
            ],
        ),
    ]