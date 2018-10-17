FROM ubuntu:16.04

MAINTAINER Weikunt <weikun.t@google.com>

RUN sed -i s@archive.ubuntu.com@mirrors.163.com@g /etc/apt/sources.list

RUN apt-get update && apt-get install software-properties-common -y \
    && add-apt-repository ppa:nginx/stable -y && apt-get update\
    && apt-get install -y build-essential python3-pip python3-dev\
    nginx libmysqlclient-dev\
    && pip3 install -i https://pypi.doubanio.com/simple uwsgi

RUN mkdir /var/www/FlaskApp && rm /etc/nginx/sites-enabled/default \
    && mkdir -p /var/log/uwsgi && mkdir /etc/uwsgi && mkdir /etc/uwsgi/vassals

COPY FlaskApp /var/www/FlaskApp/FlaskApp
COPY ./app_nginx.conf /var/www/FlaskApp/
COPY ./app_uwsgi.ini /var/www/FlaskApp/
COPY requirements.txt /var/www/FlaskApp/
COPY ./runserver.py /var/www/FlaskApp/

RUN ln -s /var/www/FlaskApp/app_uwsgi.ini /etc/uwsgi/vassals

WORKDIR /var/www/FlaskApp

RUN pip3 install -i https://pypi.doubanio.com/simple -r /var/www/FlaskApp/requirements.txt \
    && ln -s /var/www/FlaskApp/app_nginx.conf /etc/nginx/conf.d/ \
    && chown -R www-data:www-data /var/www/FlaskApp \
    && chown -R www-data:www-data /var/log

CMD /etc/init.d/nginx start && uwsgi --ini /var/www/FlaskApp/app_uwsgi.ini