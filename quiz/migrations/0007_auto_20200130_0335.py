# Generated by Django 3.0.1 on 2020-01-29 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0006_answer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='conrrect',
            new_name='correct',
        ),
    ]