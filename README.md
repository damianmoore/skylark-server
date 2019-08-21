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

If you want to help contribute or just want to avoid Docker then you can clone the repo, make virtual environment, install requirements and run the Django runserver. It will be listening on [http://localhost:8000](http://localhost:8000).

```shell
git clone https://github.com/damianmoore/skylark-server.git
pipenv install
pipenv shell
./manage.py runserver
```


## Download and register the app

There are not yet published versions in app stores as they are still being developed. You are welcome to check out and build the [Android app](https://github.com/damianmoore/skylark-android) yourself in the mean time.

Once you have the app installed you will need to connect it to a server you have running this publicly available.

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


## Logo requirements

Skylark is a mobile and desktop app that allows it's users to get notified wherever they are, when certain things happen.

It will initially be targeted at a technical audience including software engineers, administrators and electronics hobbyists who will be able to trigger alerts by inserting a small piece of code at strategic points of their processes. Some example alerts are: "Unexpected levels of traffic visiting the website", "An order has been placed, ready for dispatch", "A product matching your criteria is now available", "Motion detected in garden, security light activated", "Temperature below threshold, heater turned on".


The name is taken from the perching songbird. The Skylark is quite a dull-looking bird but has a beautiful call, nimble movements and quirky crested head plumage which it can raise or lower. It would be cool to capture some of this character but it should be distinct enough from other popular bird-related brands such as Twitter.

The graphic part of the logo should be clear enough to be identifiable when shown in the notification bar at the top of a phone in monochrome - think WhatsApp, Slack, Pinterest, Twitter, YouTube, Facebook. This probably means a square-ish bounding box for the part that's not text.

I want the app to encompass helpfulness, calming and sleekness rather than create a sense of panic as the user will interact with it many times per day. It will help them stay informed, automate areas of their life and act like a front-end to a personal assistant.

Skylark is a community-focussed project with an emphasis on security and privacy. All code is opensource for others to verify the security of and to make improvements. It might be a good idea to incorporate some of these values.
