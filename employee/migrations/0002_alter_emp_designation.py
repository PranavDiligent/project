# Generated by Django 4.1 on 2022-08-22 08:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0004_alter_accounting_year_fromdate_and_more'),
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emp',
            name='designation',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='admin_panel.designation'),
        ),
    ]
