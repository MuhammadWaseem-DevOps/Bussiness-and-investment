# Generated by Django 4.0.5 on 2022-07-03 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0006_moneyflow'),
    ]

    operations = [
        migrations.AddField(
            model_name='project_investor',
            name='percentage_equity',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4),
        ),
    ]
