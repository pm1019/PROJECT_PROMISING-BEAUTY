# Generated by Django 4.1.5 on 2023-02-28 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PRODUCT', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='p_details',
            name='p_img1',
            field=models.ImageField(null=True, upload_to='Products'),
        ),
        migrations.AddField(
            model_name='p_details',
            name='p_img2',
            field=models.ImageField(null=True, upload_to='Products'),
        ),
        migrations.AddField(
            model_name='p_details',
            name='p_img3',
            field=models.ImageField(null=True, upload_to='Products'),
        ),
        migrations.AddField(
            model_name='p_details',
            name='p_img4',
            field=models.ImageField(null=True, upload_to='Products'),
        ),
        migrations.AlterField(
            model_name='p_details',
            name='p_img',
            field=models.ImageField(null=True, upload_to='Products'),
        ),
    ]