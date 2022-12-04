# Generated by Django 4.1.3 on 2022-11-28 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Additive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, unique=True)),
            ],
            options={
                'verbose_name': 'Additive',
                'verbose_name_plural': 'Additives',
            },
        ),
        migrations.CreateModel(
            name='Allergy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, unique=True)),
            ],
            options={
                'verbose_name': 'Allergy',
                'verbose_name_plural': 'Allergies',
            },
        ),
        migrations.CreateModel(
            name='CardBalance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.DecimalField(decimal_places=2, max_digits=5)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, unique=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('main', models.BooleanField()),
            ],
            options={
                'verbose_name': 'Dish',
                'verbose_name_plural': 'Dishes',
            },
        ),
        migrations.CreateModel(
            name='DishAdditive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='DishAllergy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='DishCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='DishPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('priceStudent', models.DecimalField(decimal_places=2, max_digits=4)),
                ('priceEmployee', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='ExtDishRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('rating_avg', models.DecimalField(decimal_places=1, max_digits=2)),
                ('rating_count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Mensa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_id', models.CharField(max_length=70, unique=True)),
                ('name', models.CharField(max_length=70)),
                ('street', models.CharField(max_length=100)),
                ('houseNumber', models.CharField(max_length=20)),
                ('zipCode', models.IntegerField()),
                ('city', models.CharField(max_length=50)),
                ('startTime', models.TimeField()),
                ('endTime', models.TimeField()),
                ('lat', models.DecimalField(decimal_places=8, max_digits=13, null=True)),
                ('lon', models.DecimalField(decimal_places=8, max_digits=13, null=True)),
            ],
            options={
                'verbose_name': 'Mensa',
                'verbose_name_plural': 'Mensen',
            },
        ),
        migrations.CreateModel(
            name='UserAllergy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='UserCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='UserDishRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.FloatField()),
                ('dish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mensa.dish')),
            ],
        ),
    ]
