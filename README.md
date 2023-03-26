# Roam.io
City Events and Weather App
This Django-based web application allows users to search for events in a given city,
view events for their favorite cities, and see the weather forecast for their favorite cities. 
Users can create an account, log in, and manage their list of favorite cities.

Features
* User registration and authentication
* Event searching by city and viewing events for favorite cities
* Adding, editing, and removing favorite cities
* Displaying the weather forecast for favorite cities
* Responsive design

~Installation~
Clone the repository:

git clone https://github.com/kaietanpaul/Roam.io.git
cd Roam.io

Install the required dependencies:

pip install -r requirements.txt

Set up the PostgreSQL database in settings.py:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

Run migrations:

python manage.py migrate

Create a superuser:

python manage.py createsuperuser

Run the development server:

python manage.py runserver
Now you can access the application at http://localhost:8000.

Testing
To run tests, execute the following command:

pytest