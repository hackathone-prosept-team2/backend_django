# Generated by Django 4.2.7 on 2023-11-29 12:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dealers", "0002_auto_20231128_1528"),
    ]

    operations = [
        migrations.AddConstraint(
            model_name="dealerkey",
            constraint=models.UniqueConstraint(
                fields=("dealer_id", "key"), name="unique_pair_dealer_and_key"
            ),
        ),
    ]
