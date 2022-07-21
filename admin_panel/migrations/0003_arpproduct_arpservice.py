# Generated by Django 3.2.14 on 2022-07-21 07:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0002_auto_20220721_1300'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArpService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('hsn_code', models.CharField(max_length=100)),
                ('sale_price', models.CharField(max_length=100)),
                ('sale_price_with_tax', models.BooleanField()),
                ('tax_rate', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ArpProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('hsn_code', models.IntegerField()),
                ('product_code', models.CharField(max_length=100)),
                ('sale_price', models.CharField(max_length=100)),
                ('sale_price_with_tax', models.BooleanField()),
                ('purchase_price', models.CharField(max_length=100)),
                ('purchase_price_with_tax', models.BooleanField()),
                ('tax_rate', models.CharField(max_length=100)),
                ('opening_stock', models.CharField(max_length=100)),
                ('price_per_unit', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('minimum_stock_quantity', models.IntegerField()),
                ('unit', models.IntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_panel.category')),
            ],
        ),
    ]
