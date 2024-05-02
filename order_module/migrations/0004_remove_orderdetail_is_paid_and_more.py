# Generated by Django 4.2 on 2024-04-28 19:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product_module', '0001_initial'),
        ('order_module', '0003_orderdetail_is_paid_orderdetail_is_payment_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderdetail',
            name='is_paid',
        ),
        migrations.RemoveField(
            model_name='orderdetail',
            name='is_payment',
        ),
        migrations.RemoveField(
            model_name='orderdetail',
            name='user',
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_module.product'),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_paid', models.BooleanField(default=False)),
                ('is_payment', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
