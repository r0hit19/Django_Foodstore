# Generated by Django 3.1.7 on 2021-04-09 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0009_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='mode',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
