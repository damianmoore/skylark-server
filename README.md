# Skylark
*Phone notifications that are easy for developers to send from their scripts*

## Running the server

### Docker

Docker is the quickest way to get the server up and running. This will launch the server on localhost port 8000.

    docker run -p 8000:80 damianmoore/skylark-server:latest

### Checkout Python

If you want to help contribute or just want to avoid Docker then you can clone the repo, make virtual environment, install requirements and run the Django runserver. It will be listening on localhost port 8000.

    git clone https://github.com/damianmoore/skylark-server.git
    pipenv install
    pipenv shell
    ./manage.py runserver


## Logo requirements

Skylark is a mobile and desktop app that allows it's users to get notified wherever they are, when certain things happen.

It will initially be targeted at a technical audience including software engineers, administrators and electronics hobbyists who will be able to trigger alerts by inserting a small piece of code at strategic points of their processes. Some example alerts are: "Unexpected levels of traffic visiting the website", "An order has been placed, ready for dispatch", "A product matching your criteria is now available", "Motion detected in garden, security light activated", "Temperature below threshold, heater turned on".


The name is taken from the perching songbird. The Skylark is quite a dull-looking bird but has a beautiful call, nimble movements and quirky crested head plumage which it can raise or lower. It would be cool to capture some of this character but it should be distinct enough from other popular bird-related brands such as Twitter.

The graphic part of the logo should be clear enough to be identifiable when shown in the notification bar at the top of a phone in monochrome - think WhatsApp, Slack, Pinterest, Twitter, YouTube, Facebook. This probably means a square-ish bounding box for the part that's not text.

I want the app to encompass helpfulness, calming and sleekness rather than create a sense of panic as the user will interact with it many times per day. It will help them stay informed, automate areas of their life and act like a front-end to a personal assistant.

Skylark is a community-focussed project with an emphasis on security and privacy. All code is opensource for others to verify the security of and to make improvements. It might be a good idea to incorporate some of these values.
