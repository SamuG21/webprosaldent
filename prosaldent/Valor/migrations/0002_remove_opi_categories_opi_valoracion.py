# Generated by Django 4.0.4 on 2022-05-20 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Valor', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='opi',
            name='categories',
        ),
        migrations.AddField(
            model_name='opi',
            name='valoracion',
            field=models.ManyToManyField(related_name='get_posts', to='Valor.valor', verbose_name='Valoracion'),
        ),
    ]
