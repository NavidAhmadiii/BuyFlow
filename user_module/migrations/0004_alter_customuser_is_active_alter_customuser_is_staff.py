# Generated by Django 4.2 on 2024-04-24 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_module', '0003_alter_customuser_is_active_alter_customuser_is_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
