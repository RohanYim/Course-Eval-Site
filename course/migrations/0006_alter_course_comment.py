# Generated by Django 4.2 on 2023-04-22 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("course", "0005_alter_course_comment"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="comment",
            field=models.TextField(
                default="No comment provided", verbose_name="comment"
            ),
        ),
    ]