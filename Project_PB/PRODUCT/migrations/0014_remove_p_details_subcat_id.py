# Generated by Django 4.1.7 on 2023-03-21 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PRODUCT', '0013_p_details_subcat_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='p_details',
            name='subcat_id',
        ),
    ]