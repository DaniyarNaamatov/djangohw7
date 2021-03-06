# Generated by Django 4.0.4 on 2022-05-18 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post_app', '0002_alter_news_text'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['title'], 'verbose_name_plural': 'News'},
        ),
        migrations.CreateModel(
            name='NewsComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post_app.news')),
            ],
        ),
    ]
