# Generated by Django 2.0.5 on 2018-05-10 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paste',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('language', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('created_on', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
