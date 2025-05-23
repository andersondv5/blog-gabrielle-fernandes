# Generated by Django 5.2 on 2025-05-17 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('descricao', models.TextField()),
                ('conteudo', models.TextField()),
                ('data', models.DateField()),
            ],
        ),
    ]
