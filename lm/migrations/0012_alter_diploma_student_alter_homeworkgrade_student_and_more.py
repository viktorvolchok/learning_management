# Generated by Django 4.2.1 on 2023-05-29 21:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lm', '0011_notification_subject_alter_teacherprofile_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diploma',
            name='student',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='lm.student'),
        ),
        migrations.AlterField(
            model_name='homeworkgrade',
            name='student',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='lm.student'),
        ),
        migrations.AlterField(
            model_name='teacherprofile',
            name='phone_number',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone_number',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='student',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='lm.student'),
        ),
    ]
