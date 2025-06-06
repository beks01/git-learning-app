# Generated by Django 5.2.1 on 2025-06-03 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0002_gitcommand_language_gitlesson_language_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gitcommand',
            name='language',
            field=models.CharField(choices=[('en', 'English'), ('ru', 'Russian'), ('ge', 'German')], default='en', max_length=10),
        ),
        migrations.AlterField(
            model_name='gitlesson',
            name='language',
            field=models.CharField(choices=[('en', 'English'), ('ru', 'Russian'), ('ge', 'German')], default='en', max_length=10),
        ),
        migrations.AlterField(
            model_name='gitquiz',
            name='language',
            field=models.CharField(choices=[('en', 'English'), ('ru', 'Russian'), ('ge', 'German')], default='en', max_length=10),
        ),
    ]
