# Generated by Django 2.0.7 on 2018-07-14 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('passward', models.CharField(max_length=20)),
                ('sex', models.CharField(max_length=1)),
                ('birthday', models.CharField(max_length=10)),
            ],
        ),
    ]
