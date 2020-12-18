# Generated by Django 3.1.4 on 2020-12-18 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0006_merge_20201219_0114'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('image', models.ImageField(blank=True, default=None, upload_to='')),
                ('description', models.CharField(max_length=2000)),
                ('is_published', models.BooleanField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('website', models.URLField(blank=True, default=None)),
                ('logo', models.ImageField(blank=True, default=None, upload_to='')),
                ('is_published', models.BooleanField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='News',
        ),
    ]