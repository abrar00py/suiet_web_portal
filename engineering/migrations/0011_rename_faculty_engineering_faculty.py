# Generated by Django 4.1.3 on 2022-12-02 05:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('engineering', '0010_faculty_email_alter_faculty_designation_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Faculty',
            new_name='Engineering_Faculty',
        ),
    ]