# Generated by Django 4.2.4 on 2024-03-21 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nouapp', '0010_alter_student_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='profile/'),
        ),
    ]
