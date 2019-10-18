# Skylark

<img src="https://epixstudios.co.uk/filer/canonical/1532274227/2/" alt="Skylark Logo" width="196px" height="170px">

*Easily send notifications to your phone via HTTP*


## Running the server

### Docker

Docker is the quickest way to get the server up and running. This will launch the server on [http://localhost:8000](http://localhost:8000).

```shell
docker run -p 8000:80 damianmoore/skylark-server:latest
```

### Checkout Python

If you want to help contribute or just want to avoid Docker then you can clone the repo, make a virtual environment, install requirements and run the Django runserver. It will be listening on [http://localhost:8000](http://localhost:8000).

```shell
git clone https://github.com/damianmoore/skylark-server.git
pipenv install
pipenv shell
./manage.py runserver
```


## Download and register the app

The latest Android release is available to download from [Google Play Store](https://play.google.com/store/apps/details?id=uk.co.epixstudios.skylark).

<a href='https://play.google.com/store/apps/details?id=uk.co.epixstudios.skylark&pcampaignid=pcampaignidMKT-Other-global-all-co-prtnr-py-PartBadge-Mar2515-1'><img alt='Get it on Google Play' src='https://play.google.com/intl/en_us/badges/static/images/badges/en_badge_web_generic.png' height="64px"/></a>

You are welcome to clone and build the [Android app project](https://github.com/damianmoore/skylark-android) for yourself.

Once you have the app installed you will need to connect it to the address of an instance of the server you have running (see above).

Help would be much appreciated if you have iOS experience. We also aim to have a desktop, browser-based notification implementation.


## Sending notifications

Notification can be sent via HTTP POST or GET with data transported as JSON, POST data or URL encoding. Here are a couple of examples.

### Python (requests library)

```python
import requests
requests.post('http://localhost:8000/webhook/', params={
    'title': 'Notification from Python',
    'body': 'Sent with the requests library',
    'color': '#3776ab',
    'icon': 'https://www.python.org/static/opengraph-icon-200x200.png',
})
```

### cURL

```shell
curl -X POST \
-H "Content-Type: application/json" \
-d '{"title": "Notification from cURL", "body": "Hello, World!", "color": "#ff9500", "icon": "http://i.imgur.com/7Ih60Gu.png"}' \
http://localhost:8000/webhook/
```

<img src="https://epixstudios.co.uk/filer/canonical/1532296260/3/" alt="Screenshot of Python notification" width=50% /><img src="https://epixstudios.co.uk/filer/canonical/1532296260/4/" alt="Screenshot of cURL notification" width=50% />
