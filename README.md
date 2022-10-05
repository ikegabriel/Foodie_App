# Foodie_App
A personal Fullstack blog app built on the monolith system of Django. This app supports the features you would find on a regular blogs.<br>

# Live Site
 https://TheGabrielBlog.pythonanywhere.com

# Tools
 <img src='https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue'> <img src='https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green'>
 <img src='https://img.shields.io/badge/django%20rest-ff1709?style=for-the-badge&logo=django&logoColor=white'>
 <img src='https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E'>
 <img src='https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white'>
 <img src='https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white'>
 <img src='https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white'>
 <img src='https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white'>
 <img src='https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB'>
 <img src='https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white'>


# Database ERD
https://drawsql.app/teams/gabriels-team-1/diagrams/gabriel-s-blog

# Documentation 

# Setup
To set up this project on your local machine,<br>

1. Fork the repo and clone it to your local machine<br>

2. In your terminal, navigate to the project root folder <code>My_Blog_App</code> create a virtual environment <code>python3 -m venv env</code> , then activate it <code>source env/bin/activate</code> (<i>for linux/unix</i>) or <code>env/scripts/activate</code> (<i>for windows</i>)<br>

3. Install the project dependencies <code>pip install -r requirements.txt </code> <br>

4. Make your migrations <code>python manage.py migrate</code> or run makemigrations again if necessary <code>python manage.py makemigrations</code> <br>

5. Start the django development server <code>python manage.py runserver</code> or use the gunicorn server <code>gunicorn review_project.wsgi</code> <br>

6. Open the address given by the server in your browser. It may look something like this <code>http://127.0.0.1:8000/</code>

<br><br>
<strong>NOTE</strong><br>
* Remember to generate a generate or set a new secret key in the <code>settings.py</code> file. you can quickly generate one in the terminal by running <code>python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'</code> and set your environment variables for the <code>SECRET_KEY</code> located at <i>myblog/settings</i> and <code>key</code> in <i>blog/views.py</i><br>

* The <code>key</code> as mentioned above is an <a href='https://openweathermap.com' targer='blank'>Openweathermap<a> Api key. You can get one by creating an account on their site.
