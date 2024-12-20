# Generated by Django 4.2.16 on 2024-11-27 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=15)),
                ('age', models.IntegerField()),
                ('monthly_salary', models.FloatField()),
                ('approved_limit', models.FloatField()),
                ('current_debt', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('loan_id', models.AutoField(primary_key=True, serialize=False)),
                ('loan_amount', models.FloatField()),
                ('tenure', models.IntegerField()),
                ('interest_rate', models.FloatField()),
                ('emi_paid_on_time', models.BooleanField(default=False)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('monthly_repayment', models.FloatField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.customer')),
            ],
        ),
    ]
