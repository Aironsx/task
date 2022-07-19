# ToDo app

ToDo is an app where people can add tasks and track them.


## Applied technologies

- Language: Python
- Frameworks: Django + DRF
- DB: sqlite + redis for celery task
- Periodic task: celery + redis
- html and css has been taken from bootstrap and adjusted in frame of project
- docker, docker-compose

## Functionality

- All user registration tasks (signup, login, reset password)
- App can follow your task up, in case due date is nearly it put tasks in 
  coming soon task or when it's overdued in delayed tasks.
- API with jwt authentication

## Next step

- Telegram bot with all functionality (CRUD)
- Add possibility to send email directly to email

## Install

```
git clone git@github.com:Aironsx/Task.git
```
```
cd Task
```
```
python3 -m venv env
```
```
source/venv/bin/activate
```
```
python3 -m pip install --upgrade pip
```    
```
pip install -r requirements.txt
```   
```
python3 manage.py migrate
```       
    
## Run the app
```
python manage.py runserver
```
