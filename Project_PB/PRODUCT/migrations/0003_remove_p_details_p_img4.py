# Generated by Django 4.1.5 on 2023-02-28 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PRODUCT', '0002_p_details_p_img1_p_details_p_img2_p_details_p_img3_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='p_details',
            name='p_img4',
        ),
    ]