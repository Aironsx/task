import requests
from celery.task import task

"""
Необходимо:

1. в функции get_notification сделать проверку на токен, если устарел, 
подгрузить из бд данные пользователя и создать новый jwt токен либо
запросить у пользователя снова ввести логин и пароль и создать токен
"""

@task
def get_notification_data(jwt_token):
    headers = {'Authorization': jwt_token}
    request_data = requests.get('http://127.0.0.1:8000/api/v1/tasks/?delayed_task=True')

