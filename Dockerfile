FROM debian:stretch-slim

RUN apt-get update && \
    apt-get install -y python3-pip=9.0.1-2 supervisor=3.3.1-1+deb9u1 nginx-light=1.10.3-1+deb9u1 && \
    apt-get clean && \
        rm -rf /var/lib/apt/lists/* \
               /tmp/* \
               /var/tmp/*

COPY requirements.txt /srv/requirements.txt

RUN pip3 install -r /srv/requirements.txt

RUN mkdir -p /data

COPY manage.py /srv/manage.py
COPY skylark /srv/skylark
COPY notifications /srv/notifications

COPY run.sh /srv/run.sh
COPY supervisord.conf /etc/supervisord.conf
COPY nginx.conf /etc/nginx/nginx.conf

WORKDIR /srv
RUN python3 manage.py collectstatic --noinput --link
CMD ./run.sh

EXPOSE 80
