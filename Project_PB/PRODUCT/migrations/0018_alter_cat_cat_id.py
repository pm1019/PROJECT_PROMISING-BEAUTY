# Generated by Django 4.1.7 on 2023-03-22 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PRODUCT', '0017_alter_cat_cat_id_alter_p_details_offer_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='cat_id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]