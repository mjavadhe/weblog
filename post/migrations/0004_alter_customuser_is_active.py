# Generated by Django 5.0.7 on 2024-07-29 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_customuser_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]