# Generated by Django 3.1.7 on 2021-02-25 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Modern',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=3000)),
                ('status', models.CharField(default='New', max_length=100)),
                ('time', models.CharField(blank=True, max_length=150, null=True)),
            ],
            options={
                'verbose_name': 'Задача',
                'verbose_name_plural': 'Задачи',
                'db_table': 'articles',
            },
        ),
    ]
