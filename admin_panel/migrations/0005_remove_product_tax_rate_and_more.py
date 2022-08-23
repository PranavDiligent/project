# Generated by Django 4.0.6 on 2022-08-23 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0004_alter_accounting_year_fromdate_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='tax_rate',
        ),
        migrations.AddField(
            model_name='product',
            name='purchase_price_tax_rate',
            field=models.CharField(blank=True, choices=[('0.25', 'GST@0.25%'), ('0.25', 'IGST@0.25%'), ('3.0', 'GST@3%'), ('3.0', 'IGST@3%'), ('5.0', 'GST@5%'), ('5.0', 'IGST@5%'), ('12.0', 'GST@12%'), ('18.0', 'GST@18%'), ('18.0', 'IGST@18%'), ('28.0', 'GST@28%'), ('28.0', 'IGST@28%'), ('12.0', 'IGST@12%'), ('0.0', 'IGST@0%')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='sale_price_tax_rate',
            field=models.CharField(blank=True, choices=[('0.25', 'GST@0.25%'), ('0.25', 'IGST@0.25%'), ('3.0', 'GST@3%'), ('3.0', 'IGST@3%'), ('5.0', 'GST@5%'), ('5.0', 'IGST@5%'), ('12.0', 'GST@12%'), ('18.0', 'GST@18%'), ('18.0', 'IGST@18%'), ('28.0', 'GST@28%'), ('28.0', 'IGST@28%'), ('12.0', 'IGST@12%'), ('0.0', 'IGST@0%')], max_length=20, null=True),
        ),
    ]
