# Generated by Django 4.0.3 on 2023-12-06 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SummonerId',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summonerID', models.CharField(max_length=87)),
                ('create_date', models.DateTimeField()),
            ],
        ),
    ]
