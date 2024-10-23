# Django API with Django Rest Framework

This project is a Django API built with Django Rest Framework (DRF) that supports user management with custom roles, social authentication, and password reset functionality.

## Features

- **Custom User Roles**: Users can have one of the following roles:
  - Admin
  - Coach
  - Agent
  - Football Player

- **User Registration**:
  - Standard signup
  - Social signup via Google and Facebook

- **User Authentication**:
  - Standard login
  - Social login via Google and Facebook

- **Password Management**:
  - Password reset functionality

## Requirements

- Python 3.x
- Django 3.x or 4.x
- Django Rest Framework
- Django Allauth (for social authentication)
- dj-rest-auth (for RESTful authentication)

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/sirawtadesse/Django-Rest-Framework.git
   cd your-repo-name
   
   python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

pip install -r requirements.txt

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver

Technologies Used
Django
Django Rest Framework
Django Allauth
dj-rest-auth
PostgreSQL (or any other database you prefer)
Contributing
Fork the repository.
Create a new branch (git checkout -b feature/YourFeature).
Make your changes and commit them (git commit -m 'Add some feature').
Push to the branch (git push origin feature/YourFeature).
Create a new Pull Request.

Acknowledgments
Django Rest Framework
Django Allauth
dj-rest-auth

### Customizing the README

- Replace placeholders like `yourusername` and `your-repo-name` with your actual GitHub username and repository name.
- Adjust the list of technologies used if you incorporate additional libraries or tools.
- Provide any additional instructions or details specific to your project as necessary.

This README provides a clear and structured overview of your project, making it easy for users and contributors to understand how to get started and use the API effectively.
