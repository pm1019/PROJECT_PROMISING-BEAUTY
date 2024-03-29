# Generated by Django 4.1.5 on 2023-03-05 19:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('DASHBOARD', '0001_initial'),
        ('PRODUCT', '0003_remove_p_details_p_img4'),
    ]

    operations = [
        migrations.CreateModel(
            name='details',
            fields=[
                ('o_id', models.IntegerField(primary_key=True, serialize=False)),
                ('o_qty', models.IntegerField()),
                ('o_netamount', models.IntegerField()),
                ('o_date', models.DateField()),
                ('o_details', models.CharField(max_length=100)),
                ('o_status', models.BooleanField(default=False)),
                ('cust_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DASHBOARD.customer_details')),
                ('p_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PRODUCT.p_details')),
                ('user', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
