# Generated by Django 2.2.14 on 2020-12-07 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Tags', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_created=True, null=True)),
                ('created', models.DateTimeField(auto_created=True, null=True)),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('Autor', models.CharField(max_length=100)),
                ('tags', models.ManyToManyField(blank=True, null=True, related_name='tags', to='Tags.Tag')),
            ],
        ),
    ]
