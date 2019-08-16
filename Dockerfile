FROM debian:stretch-slim

RUN apt-get update && \
    apt-get install -y locales python3-pip supervisor nginx-light && \
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

COPY run.sh /srv/run.sh
COPY supervisord.conf /etc/supervisord.conf
COPY nginx.conf /etc/nginx/nginx.conf

RUN pipenv run python manage.py collectstatic --noinput --link
CMD ./run.sh

EXPOSE 80
