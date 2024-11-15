# LLM Powered Tutor-Chatbot

## To Run the Web app:
Check python is installed, and then create a virtual env. <br>
python --version <br>
python -m venv venv <br>

Activate the virtual env <br>
source venv/bin/activate <br>

Install django and openai <br>
pip install django <br>
pip install openai <br>

Run these two lines at the beginning <br>
(Also need to run these two lines ifyou make any changes to models.py) <br>
python manage.py makemigrations a2chatbot <br>
python manage.py migrate <br>

Include pre-registered users <br>
python manage.py shell <br>
import a2chatbot.views as views <br>
views.register_new_users() <br>
exit() <br>

Run the app <br>
python manage.py runserver <br>
Go to http://127.0.0.1:8000/ <br>
