# Generated by Django 4.0.6 on 2022-07-30 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_comment_alter_contact_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='is_solved',
        ),
    ]