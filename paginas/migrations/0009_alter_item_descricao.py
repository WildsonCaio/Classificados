# Generated by Django 4.0 on 2021-12-24 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginas', '0008_alter_item_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='descricao',
            field=models.TextField(blank=True),
        ),
    ]
