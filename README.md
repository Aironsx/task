# ToDo app

ToDo is an app where people can add tasks and track them.

## Description and which porblem this app should solve

### Problem statement:

No task track app which is free and can posibility to use shared account. I like to use Joplin but to have account which i can use in laptop, PC , and mobile phone i should pay. So i dedicded to code my own one.

### Description

You can add category, tasks, the app will track your task and send notification to you if it's comming. There is an API which you can use. Also now i code telegram bot to people can post and get information from telegram directly. It's easy to use one platform(telegram) to track and add all.


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
```
sudo docker run -p 6379:6379 --name some-redis -d redis
```
```
celery -A Task worker -l info
```
```
celery -A Task beat -l info
```
