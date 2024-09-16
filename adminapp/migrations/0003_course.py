# Generated by Django 4.2.4 on 2024-03-15 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0002_events'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=50)),
                ('question_number', models.PositiveIntegerField()),
                ('total_marks', models.PositiveIntegerField()),
            ],
        ),
    ]
