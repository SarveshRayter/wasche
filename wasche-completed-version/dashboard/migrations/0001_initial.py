# Generated by Django 2.2 on 2020-03-09 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Old_Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.CharField(default='', max_length=15000)),
                ('date_created', models.DateTimeField(editable=False)),
            ],
            options={
                'verbose_name_plural': 'Old data of orders',
            },
        ),
        migrations.CreateModel(
            name='Order_DashBoard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_orders', models.CharField(default='0', max_length=254)),
                ('ordered_dates', models.CharField(default='', max_length=15000)),
                ('overflown', models.BooleanField(default=False)),
                ('recent_date', models.CharField(default='', max_length=24)),
                ('recent_time', models.CharField(default='', max_length=24)),
                ('years', models.CharField(default='', max_length=150)),
                ('date_created', models.DateTimeField(editable=False)),
            ],
            options={
                'verbose_name_plural': 'Order DashBoards',
            },
        ),
    ]
