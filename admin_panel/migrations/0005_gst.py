# Generated by Django 3.2.14 on 2022-07-22 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0004_auto_20220722_1229'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gst',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tax', models.CharField(max_length=50)),
                ('tax_value', models.IntegerField()),
            ],
        ),
    ]
