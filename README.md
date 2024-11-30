# credit_app

Credit Approval System
The Credit Approval System is a backend API built using Python/Django, designed to handle customer registration, credit limit calculation, and loan management based on past and current loan data. This project uses background tasks for data ingestion and integrates seamlessly with a PostgreSQL database, all containerized using Docker for easy setup and deployment.

Table of Contents
Features
Project Structure
Tech Stack
Setup and Installation
Running the Application
API Endpoints
Background Tasks
Database Models
Example Requests
Future Improvements
Contributing
License
Features
Customer Registration: Automatically calculates and assigns a credit limit based on the customer's monthly income.
Loan Eligibility Check: Determines loan eligibility using historical data and provides loan interest rate recommendations.
Loan Creation: Processes loan applications and manages loan details.
View Loan Information: Retrieve detailed loan information for individual loans and all loans associated with a customer.
Data Ingestion: Background workers to ingest customer and loan data from Excel files.
Project Structure
Credit-Approval-System
│
├── Dockerfile
├── docker-compose.yml
├── manage.py
├── requirements.txt
├── customer_data.xlsx
├── loan_data.xlsx
│
├── credit_api
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   ├── views.py
│   ├── migrations/
│   └── tests.py
│
└── credit_approval_system
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    ├── wsgi.py
    ├── asgi.py
    └── views.py
Tech Stack
Backend: Python, Django, Django Rest Framework
Database: PostgreSQL
Background Tasks: background_task library
Containerization: Docker, Docker Compose
Setup and Installation
Prerequisites
Docker and Docker Compose installed on your system
Steps
Clone the Repository

Apply Migrations

docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
Run Background Tasks for Data Ingestion

re.
Request Body: customer_id, loan_amount, interest_rate, tenure
Response: Loan eligibility status and recommended interest rate.
3. Create Loan (POST /create-loan/)
Processes a new loan application for a customer.
Request Body: customer_id, loan_amount, interest_rate, tenure
Response: Loan approval status and monthly installment amount.
4. View Loan (GET /view-loan/<loan_id>/)
Retrieves detailed information about a specific loan.
Response: Loan details and associated customer information.
5. View Loans by Customer (GET /view-loans/<customer_id>/)
Lists all loans associated with a specific customer.
Response: A list of loan details.
Background Tasks
The project uses background tasks to ingest data from customer_data.xlsx and loan_data.xlsx.
Libraries Used: background_task

}
Future Improvements
Implement a frontend for better user experience.
Enhance loan eligibility logic to consider more factors.
Integrate automated testing for improved reliability.
Add authentication and authorization for secure API access.
Contributing
Contributions are welcome! Please fork the repository and submit a pull request.
