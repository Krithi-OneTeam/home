# Generated by Django 4.2.1 on 2023-05-19 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.CharField(max_length=220)),
                ('ename', models.CharField(max_length=220)),
                ('eemail', models.EmailField(max_length=254)),
                ('econtact', models.CharField(max_length=220)),
            ],
            options={
                'db_table': 'employee',
            },
        ),
    ]
