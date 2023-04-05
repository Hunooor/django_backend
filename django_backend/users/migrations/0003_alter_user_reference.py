# Generated by Django 4.2 on 2023-04-05 16:52

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_reference'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='reference',
            field=models.TextField(default=uuid.uuid4, unique=True),
        ),
    ]
