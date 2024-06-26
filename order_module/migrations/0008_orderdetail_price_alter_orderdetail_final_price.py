# Generated by Django 4.2 on 2024-05-02 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_module', '0007_order_order_detail'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdetail',
            name='price',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='final_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
