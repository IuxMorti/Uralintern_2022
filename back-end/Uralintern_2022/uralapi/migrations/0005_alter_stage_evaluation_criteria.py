# Generated by Django 3.2.8 on 2023-03-20 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uralapi', '0004_auto_20230313_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stage',
            name='evaluation_criteria',
            field=models.ManyToManyField(default=(), to='uralapi.EvaluationCriteria', verbose_name='Критерии оценки'),
        ),
    ]