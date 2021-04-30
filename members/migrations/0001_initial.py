# Generated by Django 3.2 on 2021-04-29 06:59

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Legs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('legs_type', models.CharField(choices=[('people', 'people'), ('cat', 'cat'), ('dog', 'dog'), ('another', 'another')], default='people', max_length=10, verbose_name='legs type')),
                ('legs_gender', models.CharField(blank=True, max_length=10)),
                ('legs_feature', models.TextField(blank=True, max_length=5000, verbose_name='특색')),
                ('legs_language', models.CharField(blank=True, max_length=10)),
                ('legs_neuter', models.BooleanField(default=False, verbose_name='중성화여부')),
                ('legs_color', models.CharField(blank=True, max_length=100)),
                ('legs_sleep_time', models.FloatField()),
                ('legs_talent', models.TextField(blank=True, max_length=5000, verbose_name='재능')),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_name', models.CharField(max_length=32, unique=True)),
                ('member_birthday', models.DateField(default=django.utils.timezone.now)),
                ('member_description', models.TextField(blank=True, max_length=1000, verbose_name='왱알왱알')),
                ('member_regular', models.BooleanField(default=False, verbose_name='중성화여부')),
                ('member_legs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.legs')),
            ],
        ),
    ]