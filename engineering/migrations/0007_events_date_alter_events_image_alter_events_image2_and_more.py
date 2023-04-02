# Generated by Django 4.0.3 on 2022-11-20 09:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('engineering', '0006_events'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='events',
            name='Image',
            field=models.ImageField(upload_to='static/img/Engineeringimage'),
        ),
        migrations.AlterField(
            model_name='events',
            name='Image2',
            field=models.ImageField(blank=True, upload_to='static/img/Engineeringimage'),
        ),
        migrations.AlterField(
            model_name='events',
            name='Image3',
            field=models.ImageField(blank=True, upload_to='static/img/Engineeringimage'),
        ),
        migrations.AlterField(
            model_name='events',
            name='Image4',
            field=models.ImageField(blank=True, upload_to='static/img/Engineeringimage'),
        ),
        migrations.AlterField(
            model_name='events',
            name='Image5',
            field=models.ImageField(blank=True, upload_to='static/img/Engineeringimage'),
        ),
        migrations.AlterField(
            model_name='events',
            name='Image6',
            field=models.ImageField(blank=True, upload_to='static/img/Engineeringimage'),
        ),
    ]
