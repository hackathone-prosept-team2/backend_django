# Generated by Django 4.2.7 on 2023-11-29 20:56

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("prices", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="dealerprice",
            options={
                "ordering": ("-date",),
                "verbose_name": "Цена дилера",
                "verbose_name_plural": "Цены дилеров",
            },
        ),
    ]
