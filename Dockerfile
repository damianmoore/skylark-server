FROM debian:buster-slim

RUN apt-get update && \
    apt-get install -y locales python3-pip python3-dev default-libmysqlclient-dev supervisor nginx-light && \
    apt-get clean && \
        rm -rf /var/lib/apt/lists/* \
               /tmp/* \
               /var/tmp/*

RUN echo "en_GB.UTF-8 UTF-8" > /etc/locale.gen && locale-gen
ENV LANG en_GB.UTF-8
ENV LANGUAGE en_GB:en
ENV LC_ALL en_GB.UTF-8

WORKDIR /srv

COPY Pipfile /srv/Pipfile
RUN pip3 install pipenv
RUN pipenv install --skip-lock

RUN mkdir -p /data

COPY manage.py /srv/manage.py
COPY skylark /srv/skylark
COPY notifications /srv/notifications

COPY system /srv/system

RUN pipenv run python manage.py collectstatic --noinput --link

CMD ./system/run.sh

EXPOSE 80
