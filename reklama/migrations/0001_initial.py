# Generated by Django 4.2.3 on 2023-07-09 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reklama',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Reklama nomini kiriting', max_length=600, verbose_name='Reklama nomi')),
                ('image', models.ImageField(help_text='Reklama rasmini yuklang', upload_to='reklama-images', verbose_name='Reklama rasmi')),
                ('description', models.TextField(help_text='Reklama haqida kiriting', verbose_name='Reklama haqida qisqacha')),
                ('viewed', models.IntegerField(blank=True, help_text="Ko'rilganlari soni", null=True, verbose_name="Ko'rilganlari soni")),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Reklama ',
                'verbose_name_plural': 'Reklamalar ',
                'db_table': 'Reklama',
            },
        ),
    ]
