# Generated by Django 4.2.2 on 2024-03-10 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chairman',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('Description', models.TextField(max_length=100)),
                ('image', models.ImageField(upload_to='chairman/')),
            ],
        ),
        migrations.CreateModel(
            name='DirectorBoard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='director board/')),
            ],
        ),
        migrations.CreateModel(
            name='ManagementCouncil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='management council/')),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('Description', models.TextField(max_length=100)),
                ('image', models.ImageField(upload_to='manager/')),
            ],
        ),
        migrations.CreateModel(
            name='MCQA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Description', models.TextField(max_length=100)),
                ('Document', models.FileField(upload_to='mcqa/')),
            ],
        ),
        migrations.CreateModel(
            name='MCQAmember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('Image', models.ImageField(upload_to='mcqa/')),
            ],
        ),
        migrations.CreateModel(
            name='Principal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('Description', models.TextField(max_length=100)),
                ('image', models.ImageField(upload_to='manager/')),
            ],
        ),
    ]
