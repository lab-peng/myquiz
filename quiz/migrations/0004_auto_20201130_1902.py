# Generated by Django 3.1.3 on 2020-11-30 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_remove_quiz_question_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='option5',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='answer',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='option1',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='option2',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='option3',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='option4',
            field=models.CharField(max_length=100),
        ),
    ]
