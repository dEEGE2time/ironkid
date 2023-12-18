# Generated by Django 4.2.8 on 2023-12-18 19:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0003_alter_product_size"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="size",
            field=models.IntegerField(
                choices=[
                    ("XS", 0),
                    ("S", 1),
                    ("M", 2),
                    ("L", 3),
                    ("XL", 4),
                    ("XXL", 5),
                ],
                default=0,
            ),
        ),
    ]
