# Generated by Django 4.1.1 on 2022-10-31 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("jobs", "0002_alter_company_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="company",
            name="type",
            field=models.CharField(
                choices=[("IS", "INTERNSHIP"), ("FT", "FULLTIME"), ("PT", "PARTTIME")],
                default="FT",
                max_length=2,
            ),
        ),
    ]
