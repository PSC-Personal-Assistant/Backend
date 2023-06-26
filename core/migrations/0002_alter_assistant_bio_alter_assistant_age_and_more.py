# Generated by Django 4.2.2 on 2023-06-26 16:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="assistant",
            name="Bio",
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name="assistant",
            name="age",
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name="assistant",
            name="disability",
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name="assistant",
            name="experience",
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name="assistant",
            name="height",
            field=models.PositiveSmallIntegerField(
                help_text="in centimeters", null=True
            ),
        ),
        migrations.AlterField(
            model_name="assistant",
            name="identity",
            field=models.CharField(
                choices=[
                    ("NIN", "NIN"),
                    ("Passport", "Passport"),
                    ("VIN", "Voters Card"),
                ],
                max_length=500,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="assistant",
            name="qualifications",
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name="assistant",
            name="services",
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name="baseuser",
            name="location",
            field=models.TextField(null=True),
        ),
    ]