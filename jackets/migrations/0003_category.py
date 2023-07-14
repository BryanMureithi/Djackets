# Generated by Django 4.2.2 on 2023-07-03 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jackets', '0002_jacket_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]