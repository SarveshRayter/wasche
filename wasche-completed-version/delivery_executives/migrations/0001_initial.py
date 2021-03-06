# Generated by Django 2.2 on 2020-03-09 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contracts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deliver_Executive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('phone_number', models.CharField(default='', max_length=20)),
                ('address', models.CharField(default='', max_length=254)),
                ('qr_code_data', models.BinaryField()),
                ('date_joined', models.DateTimeField(editable=False)),
                ('contract_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contracts.Contracts')),
            ],
            options={
                'verbose_name_plural': 'Delivery Exceutive Details',
            },
        ),
        migrations.CreateModel(
            name='ongoing_delivery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('on_going', models.CharField(default='', max_length=24)),
                ('date_started', models.DateTimeField(editable=False)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='delivery_executives.Deliver_Executive')),
            ],
            options={
                'verbose_name_plural': 'Ongoing Delivery Details',
            },
        ),
    ]
