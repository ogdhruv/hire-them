# Generated by Django 4.1.1 on 2022-10-16 06:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("rooms", "0002_message_room_topic_delete_company_message_room_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="room",
            name="topic",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="rooms.topic",
            ),
        ),
    ]
