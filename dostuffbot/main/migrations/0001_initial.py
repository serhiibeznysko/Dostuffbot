# Generated by Django 2.1.7 on 2019-04-04 06:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('token', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=128)),
                ('last_name', models.CharField(blank=True, max_length=128, null=True)),
                ('username', models.CharField(blank=True, max_length=128, null=True)),
                ('lang', models.CharField(blank=True, max_length=10, null=True)),
                ('is_bot', models.BooleanField(default=False)),
                ('dialog_id', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='bot',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bot_set', to='main.User'),
        ),
    ]
