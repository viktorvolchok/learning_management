# Generated by Django 4.2.1 on 2023-05-29 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lm', '0008_notification_userprofile_teacherprofile_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homeworkgrade',
            name='grade',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='age',
            field=models.IntegerField(),
        ),
    ]
