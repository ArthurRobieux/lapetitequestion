# Generated by Django 3.2 on 2020-10-23 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_remove_choice_votes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='poll',
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='polls.question'),
        ),
    ]
