# Generated by Django 4.0.5 on 2022-07-02 20:06

from django.db import migrations, models
import embed_video.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Preaching',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_teaching', models.CharField(max_length=350)),
                ('youtube', embed_video.fields.EmbedVideoField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
