# Generated by Django 3.0.8 on 2020-07-22 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0002_transacao'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transacao',
            options={'verbose_name_plural': 'Transação'},
        ),
        migrations.AlterField(
            model_name='transacao',
            name='data',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='transacao',
            name='observacao',
            field=models.TextField(blank=True, null=True),
        ),
    ]
