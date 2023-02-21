# Generated by Django 4.1.5 on 2023-02-21 09:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('DASHBOARD', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('cat_id', models.IntegerField(primary_key=True, serialize=False)),
                ('cat_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('offer_id', models.IntegerField(primary_key=True, serialize=False)),
                ('offer_name', models.TextField(max_length=30)),
                ('offer_desc', models.TextField(max_length=150)),
                ('offer_start_date', models.DateField()),
                ('offer_end_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='SubCat',
            fields=[
                ('subcat_id', models.IntegerField(primary_key=True, serialize=False)),
                ('subcat_name', models.CharField(max_length=50)),
                ('cat_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.SET_DEFAULT, to='PRODUCT.cat')),
            ],
        ),
        migrations.CreateModel(
            name='P_Details',
            fields=[
                ('product_id', models.IntegerField(primary_key=True, serialize=False)),
                ('p_name', models.CharField(max_length=50)),
                ('p_price', models.IntegerField()),
                ('p_label', models.CharField(default='NEW', max_length=20)),
                ('p_qty', models.IntegerField()),
                ('p_type', models.CharField(max_length=30)),
                ('p_fabric', models.CharField(max_length=30)),
                ('p_size', models.CharField(max_length=30)),
                ('p_img', models.ImageField(upload_to='Products')),
                ('p_desc', models.CharField(max_length=100)),
                ('p_color', models.CharField(max_length=50)),
                ('offer_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.SET_DEFAULT, to='PRODUCT.offer')),
                ('subcat_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.SET_DEFAULT, to='PRODUCT.subcat')),
            ],
        ),
        migrations.CreateModel(
            name='Add_to_cart',
            fields=[
                ('cart_id', models.IntegerField(primary_key=True, serialize=False)),
                ('cart_qty', models.IntegerField(default=1)),
                ('cust_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.SET_DEFAULT, to='DASHBOARD.customer_details')),
                ('p_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.SET_DEFAULT, to='PRODUCT.p_details')),
            ],
        ),
    ]
