# Generated by Django 4.2.5 on 2023-09-16 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('user_type', models.CharField(max_length=50)),
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]
