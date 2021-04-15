# Generated by Django 3.1.4 on 2021-04-02 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20210331_0756'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=300)),
                ('price', models.FloatField()),
                ('img', models.ImageField(upload_to='pics')),
            ],
        ),
    ]
