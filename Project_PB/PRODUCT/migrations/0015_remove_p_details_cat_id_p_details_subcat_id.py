# Generated by Django 4.1.7 on 2023-03-21 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PRODUCT', '0014_remove_p_details_subcat_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='p_details',
            name='cat_id',
        ),
        migrations.AddField(
            model_name='p_details',
            name='subcat_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.SET_DEFAULT, to='PRODUCT.subcat'),
        ),
    ]
