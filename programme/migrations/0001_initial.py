# Generated by Django 4.1.6 on 2023-02-17 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_Album', models.CharField(max_length=100)),
                ('pochette', models.FileField(help_text='pochette de l album', upload_to='pochette')),
                ('desciption', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Evenements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_evenement', models.CharField(max_length=100)),
                ('imgages', models.FileField(help_text='images de l evenements', upload_to='imagesEvenements')),
            ],
        ),
        migrations.CreateModel(
            name='Titre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_titre', models.CharField(max_length=100)),
                ('Album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='album', to='programme.album')),
            ],
        ),
    ]
