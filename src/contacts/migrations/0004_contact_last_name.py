# Generated by Django 4.0.1 on 2022-02-01 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contacts", "0003_rename_contact_picture_contact_contact_image_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="contact",
            name="last_name",
            field=models.CharField(default=1, max_length=25),
            preserve_default=False,
        ),
    ]
