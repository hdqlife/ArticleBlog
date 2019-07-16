# Generated by Django 2.2.1 on 2019-06-02 17:05

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
                ('label', models.CharField(max_length=32)),
                ('desctiption', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('desctiption', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('author', models.CharField(max_length=32)),
                ('desctiption', ckeditor.fields.RichTextField()),
                ('content', ckeditor.fields.RichTextField()),
                ('time', models.DateField()),
                ('picture', models.ImageField(upload_to='images')),
                ('tui', models.IntegerField()),
                ('click', models.IntegerField()),
                ('types', models.ForeignKey(on_delete=True, to='Article.Type')),
            ],
        ),
    ]
