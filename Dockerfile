FROM tiangolo/uwsgi-nginx-flask:python3.8

COPY ./app /app

ENV FLASK_ENV=development

#docker build -t myimage .
#docker run -d --name mycontainer -p 80:80 myimage