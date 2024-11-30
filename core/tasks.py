import pandas as pd
from .models import Customer, Loan
from celery import shared_task

@shared_task
def import_customer_data(file_path):
    data = pd.read_excel(file_path)
    for _, row in data.iterrows():
        Customer.objects.create(
            first_name=row['first_name'],
            last_name=row['last_name'],
            phone_number=row['phone_number'],
            monthly_salary=row['monthly_salary'],
            approved_limit=row['approved_limit'],
            current_debt=row['current_debt'],
        )

@shared_task
def import_loan_data(file_path):
    data = pd.read_excel(file_path)
    for _, row in data.iterrows():
        Loan.objects.create(
            customer_id=row['customer id'],
            loan_amount=row['loan amount'],
            tenure=row['tenure'],
            interest_rate=row['interest rate'],
            emi_paid_on_time=row['EMIs paid on time'],
            start_date=row['start date'],
            end_date=row['end date'],
            monthly_repayment=row['monthly repayment (emi)'],
        )
