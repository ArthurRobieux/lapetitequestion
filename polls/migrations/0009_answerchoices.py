# Generated by Django 3.2 on 2020-10-23 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_remove_answer_choice_ids'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerChoices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_id', models.IntegerField()),
                ('answer', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='polls.answer')),
            ],
        ),
    ]