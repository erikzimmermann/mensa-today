# Generated by Django 4.1.3 on 2022-12-20 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_usercourse_alter_course_users'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='courses',
            field=models.ManyToManyField(through='courses.UserCourse', to='courses.course'),
        ),
    ]