# Generated by Django 4.0.5 on 2022-07-09 19:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Partner', '0003_event_new'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Contibute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('categories', models.ManyToManyField(to='Partner.category')),
                ('partner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Partner.partner')),
            ],
            options={
                'ordering': ('-date_created',),
            },
        ),
    ]
