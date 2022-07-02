# Generated by Django 3.2 on 2022-07-02 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project_investor',
            name='percentage_equity',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4),
        ),
        migrations.AlterField(
            model_name='shares',
            name='percentage_equity',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4),
        ),
    ]
