# Generated by Django 3.0.8 on 2020-07-27 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='')),
                ('time', models.TimeField(verbose_name='')),
                ('mood', models.CharField(max_length=20, verbose_name='')),
                ('entry', models.TextField(verbose_name='')),
            ],
        ),
    ]
