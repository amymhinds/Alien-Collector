# Generated by Django 2.2.6 on 2019-12-17 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_testsubjects'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ufo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=50)),
            ],
        ),
    ]
