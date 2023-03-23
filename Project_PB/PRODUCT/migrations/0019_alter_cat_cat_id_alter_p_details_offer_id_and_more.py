# Generated by Django 4.1.7 on 2023-03-22 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PRODUCT', '0018_alter_cat_cat_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='cat_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='p_details',
            name='offer_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.SET_DEFAULT, to='PRODUCT.offer'),
        ),
        migrations.AlterField(
            model_name='subcat',
            name='subcat_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]