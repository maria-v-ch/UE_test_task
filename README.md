# PRODUCTS & TARIFFS & PROMOTIONS API

## Overview
This project is a Django-based application designed to manage products, tariffs, and promotions. It provides an API 
that returns product information along with applicable tariffs and promotions in XML format.

## Installation
To set up this project locally, follow these steps:

**1. Clone the Repository**


    git clone https://github.com/maria-v-ch/UE_test_task
    cd UE_test_task

**2. Create a Virtual Environment**

    python -m venv env

**3. Activate the Virtual Environment**

On Windows:

    env\Scripts\activate

On macOS/Linux:

    source env/bin/activate

**4. Install Dependencies**

    pip install -r requirements.txt


## Configuration

**1. Create a `.env` File**

Create a .env file in the root directory of the project and include your environment-specific settings. 
Read  `.env.example` for the example data.

**2. Run Migrations**

Create the necessary database tables:

    python manage.py makemigrations
    python manage.py migrate

**3. Create a Superuser**

Set up an admin user for accessing the Django admin interface:

    python manage.py createsuperuser

Follow the prompts to create the superuser account.

## Usage

**1. Start the Development Server**

    python manage.py runserver

**2. Access the API**

You can access the API at:

    http://127.0.0.1:8000/api/products-tariffs

This endpoint provides XML output of products, tariffs, and promotions.

## Testing

Run the test suite to ensure everything is working correctly:

    python manage.py test









# UE_test_task
