# Generated by Django 4.0.3 on 2022-03-09 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sklepApp', '0023_alter_produkt_data_dodania_alter_produkt_opis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produkt',
            name='opis',
            field=models.TextField(default='opis_domyśłny'),
        ),
    ]
