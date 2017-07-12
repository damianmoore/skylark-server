import json
from json.decoder import JSONDecodeError

from django.http import JsonResponse
from django.template import engines
from django.views.decorators.csrf import csrf_exempt
from pyfcm import FCMNotification

from .models import Device, Notification, Filter


push_service = FCMNotification(api_key='AAAAyBt3BfQ:APA91bH3Sikwk947G8DAxqfin-vYgLZOJT_4mnOOQ56-M3JqRadXXo_qpRdeFzchirBqZmPiB2nqNZLIc_rcvcSOJ4jPPkplfAmtI-mAYtuvfjkBqdwUpS1wQzjOgpc4qVrnbY2QjwxD')


@csrf_exempt
def api_register(request):
    request_data = json.loads(request.read().decode('utf-8'))
    if 'id' in request_data:
        device = Device.objects.get(id=request_data['id'])
        if 'firebase_token' in request_data:
            device.firebase_token = request_data['firebase_token']
        if 'name' in request_data:
            device.name = request_data['name']
        device.save()
    else:
        device = Device()
        device.name = request_data['name']
        device.save()
    return JsonResponse({'id': device.id})


@csrf_exempt
def api_notification(request):
    request_data = json.loads(request.read().decode('utf-8'))
    response_data = {}

    if 'id' in request_data:
        notification = Notification.objects.get(id=request_data['id'])
        response_data = {
            'id': notification.id,
            'title': notification.title,
            'body': notification.body,
            'icon': notification.icon,
            'color': notification.color,
            'webhook': notification.webhook,
        }

    return JsonResponse(response_data)


@csrf_exempt
def webhook(request, name=None):
    try:
        request_data = json.loads(request.read().decode('utf-8'))
    except JSONDecodeError:
        request_data = request.GET
        request_data.update(request.POST)

    notification_data = {
        'title': 'Unfiltered ' + name + ' notification',
        'webhook': name,
        'raw_data': json.dumps(request_data),
    }

    if name:
        try:
            notification_filter = Filter.objects.get(name=name)
            django_engine = engines['django']
            for key in ['title', 'body', 'icon', 'color']:
                template = django_engine.from_string(getattr(notification_filter, key))
                notification_data[key] = template.render(request_data)

        except Filter.DoesNotExist:
            pass

    notification = Notification(**notification_data)
    notification.save()

    status = 'ERROR'
    registration_ids = [device.firebase_token for device in Device.objects.all()]

    if registration_ids:
        data_message = {
            'title': notification.title,
            'body': notification.body,
            'icon': notification.icon,
            'color': notification.color,
            'webhook': notification.webhook,
        }
        result = push_service.notify_multiple_devices(registration_ids=registration_ids, data_message=data_message)

        if result[0]['success'] == 1:
            status = 'OK'

    return JsonResponse({'status': status})
