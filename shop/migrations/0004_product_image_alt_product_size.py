# Generated by Django 4.2.8 on 2023-12-17 14:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0003_auto_20231211_1548"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="image_alt",
            field=models.CharField(default="alt", max_length=100),
        ),
        migrations.AddField(
            model_name="product",
            name="size",
            field=models.IntegerField(
                choices=[
                    (0, "XS"),
                    (1, "S"),
                    (2, "M"),
                    (3, "L"),
                    (4, "XL"),
                    (5, "XXL"),
                ],
                default=0,
            ),
        ),
    ]
