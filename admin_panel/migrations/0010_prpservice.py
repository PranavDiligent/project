# Generated by Django 3.2.14 on 2022-07-22 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0009_auto_20220722_1332'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrpService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('hsn_code', models.CharField(max_length=100)),
                ('service_code', models.CharField(max_length=50)),
                ('service_price', models.CharField(max_length=100)),
            ],
        ),
    ]
