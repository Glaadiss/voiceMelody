FROM python:3.7-slim-stretch
ENV PYTHONUNBUFFERED 1
WORKDIR /code

RUN apt-get update && apt-get install -y git python3-dev gcc libsndfile1 ffmpeg

COPY requirements.txt /code/
RUN pip install --upgrade -r requirements.txt

COPY . /code/

# RUN python manage.py makemigrations
# RUN python manage.py migrate
EXPOSE 8000
# CMD ["python", "manage.py", "runserver"]
