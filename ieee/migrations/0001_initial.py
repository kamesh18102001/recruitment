# Generated by Django 3.1.1 on 2020-09-06 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('gender', models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE')], max_length=6)),
                ('dob', models.DateField()),
                ('branch', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=50)),
            ],
        ),
    ]
