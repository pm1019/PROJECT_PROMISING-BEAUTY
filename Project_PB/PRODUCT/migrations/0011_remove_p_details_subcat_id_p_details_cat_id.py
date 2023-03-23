# Generated by Django 4.1.7 on 2023-03-21 12:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PRODUCT', '0010_delete_accessories_delete_bag_delete_cosmetics_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='p_details',
            name='subcat_id',
        ),
        migrations.AddField(
            model_name='p_details',
            name='cat_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.SET_DEFAULT, to='PRODUCT.cat'),
        ),
    ]
