# Generated by Django 4.0.1 on 2022-01-29 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_auto_20171227_2246"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="first_name",
            field=models.CharField(
                blank=True, max_length=150, verbose_name="first name"
            ),
        ),
    ]
