# Generated by Django 4.1.3 on 2023-01-04 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Answer',
            new_name='Choice',
        ),
        migrations.AlterField(
            model_name='question',
            name='date_pub',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date published'),
        ),
    ]
