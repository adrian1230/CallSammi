# Generated by Django 3.0.4 on 2020-03-09 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('source', models.CharField(blank=True, max_length=200, null=True)),
                ('original_text', models.TextField()),
                ('summarized_text', models.TextField(blank=True, null=True)),
                ('category', models.CharField(choices=[('healthcare', 'healthcare'), ('technology', 'technology'), ('science', 'science'), ('beauty', 'beauty'), ('entertainment', 'entertainment'), ('politic', 'politic'), ('culinary', 'culinary'), ('others', 'others')], max_length=70)),
                ('user', models.CharField(blank=True, max_length=100, null=True)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
