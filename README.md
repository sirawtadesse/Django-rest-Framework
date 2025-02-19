🔗 Django API with Django Rest Framework (DRF)
This project is a Django API built with Django Rest Framework (DRF) that provides user management, custom roles, social authentication, and password reset functionality.

🌟 Features
✅ Custom User Roles:

Admin
Coach
Agent
Football Player
✅ User Registration & Authentication:

Standard signup & login
Social authentication (Google, Facebook)
✅ Password Management:

Password reset functionality
✅ Security & Authentication:

JWT-based authentication
Token refresh mechanism
✅ RESTful API Endpoints:

User management
Role-based access control
Authentication & authorization
🚀 Tech Stack
Backend: Django, Django Rest Framework
Authentication: Django Allauth, dj-rest-auth
Database: PostgreSQL (or any preferred database)
Social Login: Google & Facebook OAuth
Deployment: Docker, AWS, DigitalOcean
⚡ Installation & Setup
1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/sirawtadesse/Django-Rest-Framework.git
cd Django-Rest-Framework
2️⃣ Set Up Virtual Environment
bash
Copy
Edit
python -m venv venv  
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4️⃣ Apply Migrations
bash
Copy
Edit
python manage.py migrate
5️⃣ Create Superuser
bash
Copy
Edit
python manage.py createsuperuser
6️⃣ Run the Development Server
bash
Copy
Edit
python manage.py runserver
Access API at http://127.0.0.1:8000

🛠 API Endpoints
Endpoint	Method	Description
/api/auth/register/	POST	User registration
/api/auth/login/	POST	User login
/api/auth/logout/	POST	Logout
/api/auth/password/reset/	POST	Password reset
/api/users/	GET	List all users
/api/users/{id}/	GET	Get user details
📜 Contribution Guide
💡 We welcome contributions! Follow these steps to contribute:

Fork the repository
Create a new branch
bash
Copy
Edit
git checkout -b feature/YourFeature
Make your changes and commit
bash
Copy
Edit
git commit -m "Add new feature"
Push to GitHub
bash
Copy
Edit
git push origin feature/YourFeature
Create a Pull Request (PR)
📬 Contact & Support
📍 Developer: Siraw Tadesse
📧 Email: sirawbizutadesse21@gmail.com
💼 GitHub: github.com/sirawtadesse

⭐ If you find this project useful, give it a star! 🚀

