# Generated by Django 3.2 on 2020-10-23 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_answer_choice_ids'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='choice_ids',
        ),
    ]
