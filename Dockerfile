FROM python:3.7-slim-stretch
ENV PYTHONUNBUFFERED 1
WORKDIR /code

RUN apt-get update && apt-get install -y git python3-dev gcc

COPY requirements.txt /code/
RUN pip install --upgrade -r requirements.txt

COPY . /code/

# RUN python manage.py makemigrations
# RUN python manage.py migrate
# ADD ffmpeg-git-20191121-amd64-static/ /usr/local/bin
RUN pip install spleeter
EXPOSE 8000
RUN apt-get install -y libsndfile1
RUN apt-get install -y ffmpeg
# RUN pip install sndfile
# CMD ["python", "manage.py", "runserver"]
