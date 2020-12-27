# Generated by Django 3.0.6 on 2020-11-11 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('items_json', models.CharField(max_length=5000)),
                ('name', models.CharField(max_length=90)),
                ('email', models.CharField(max_length=90)),
                ('address', models.CharField(max_length=90)),
                ('city', models.CharField(max_length=90)),
                ('state', models.CharField(max_length=90)),
                ('zip_code', models.CharField(max_length=90)),
            ],
        ),
    ]
