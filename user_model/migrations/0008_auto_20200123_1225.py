# Generated by Django 3.0.2 on 2020-01-23 09:25

from django.db import migrations, models
import user_model.models


class Migration(migrations.Migration):

    dependencies = [
        ('user_model', '0007_auto_20200122_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='date_pub',
            field=models.DateTimeField(default=user_model.models.get_now),
        ),
    ]
