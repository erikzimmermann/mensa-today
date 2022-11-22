# Generated by Django 4.1.3 on 2022-11-16 15:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0002_remove_timeslot_unique appversion_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=80)),
                ('seats', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='timeslot',
            name='endDate',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='timeslot',
            name='startDate',
            field=models.DateField(null=True),
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.room')),
                ('timeslot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.timeslot')),
            ],
        ),
    ]
