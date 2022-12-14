# Generated by Django 4.1.3 on 2023-01-10 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('publishId', models.BigIntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('learnweb_abbr', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=80)),
                ('seats', models.IntegerField(null=True)),
                ('lon', models.DecimalField(decimal_places=8, max_digits=13, null=True)),
                ('lat', models.DecimalField(decimal_places=8, max_digits=13, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RoomMensaDistance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distance', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Timeslot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weekDay', models.CharField(max_length=50)),
                ('startTime', models.TimeField()),
                ('endTime', models.TimeField()),
                ('startDate', models.DateField(null=True)),
                ('endDate', models.DateField(null=True)),
                ('rythm', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='UserCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crawl_date', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
            ],
        ),
    ]
