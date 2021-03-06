# Generated by Django 4.0.5 on 2022-07-03 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0005_project_cro_project_registration_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MoneyFlow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_profit_project', models.DecimalField(decimal_places=2, default=0, max_digits=4)),
                ('business_loss_project', models.DecimalField(decimal_places=2, default=0, max_digits=4)),
                ('investor_profit', models.DecimalField(decimal_places=2, default=0, max_digits=4)),
                ('investor_loss', models.DecimalField(decimal_places=2, default=0, max_digits=4)),
                ('monthly_cost', models.IntegerField(default=0)),
                ('monthly_earning', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='business.project')),
                ('project_investor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='business.project_investor')),
            ],
        ),
    ]
