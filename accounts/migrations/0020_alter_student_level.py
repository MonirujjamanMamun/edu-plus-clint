# Generated by Django 5.0.6 on 2024-06-03 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0019_user_gender"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="level",
            field=models.CharField(
                choices=[("SSC", "SSC"), ("HSC", "HSC")], max_length=25, null=True
            ),
        ),
    ]
