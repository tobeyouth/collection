FROM ubuntu
MAINTAINER tobeyouth <tobeyouth@gmail.com>

# copy from p0bailey/docker-flask
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update

RUN apt-get install -y uwsgi
RUN apt-get install -y python-pip 
RUN apt-get install -y nginx 
RUN apt-get install -y supervisor

COPY nginx/flask.conf /etc/nginx/sites-available/
COPY supervisor/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY app /var/www/app

# install deps
ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

RUN mkdir -p /var/log/nginx/app /var/log/uwsgi/app /var/log/supervisor \
    && rm /etc/nginx/sites-enabled/default \
    && ln -s /etc/nginx/sites-available/flask.conf /etc/nginx/sites-enabled/flask.conf \
    && echo "daemon off;" >> /etc/nginx/nginx.conf \
    && chown -R www-data:www-data /var/www/app \
    && chown -R www-data:www-data /var/log \
    && service mysql start

# node env
RUN apt-get install -y nodejs

CMD ["/usr/bin/supervisord"]
