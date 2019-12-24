# Generated by Django 2.2.7 on 2019-11-17 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.CharField(max_length=20)),
                ('pname', models.CharField(max_length=100)),
                ('pprice', models.IntegerField()),
            ],
            options={
                'db_table': 'products',
            },
        ),
    ]
