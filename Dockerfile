FROM python:3.8

WORKDIR /usr/src/task

RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/requirements.txt
RUN pip install -r /usr/src/requirements.txt

COPY . /usr/src/task

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]