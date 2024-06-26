# Generated by Django 5.0.4 on 2024-04-04 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=24)),
                ('description', models.TextField()),
                ('type', models.CharField(choices=[('Cardio', 'Кардио'), ('Strength', 'Силовые'), ('Stretching', 'Растяжка')], max_length=12)),
                ('level', models.CharField(choices=[('Beginner', 'Начинающий'), ('Intermediate', 'Средний'), ('Advanced', 'Продвинутый')], max_length=12)),
                ('duration', models.DurationField()),
                ('reps', models.IntegerField()),
                ('sets', models.IntegerField()),
            ],
        ),
    ]
