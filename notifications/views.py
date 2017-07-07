import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from pyfcm import FCMNotification

from .models import Device


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
def webhook(request):
    request_data = json.loads(request.read().decode('utf-8'))

    registration_ids = [device.firebase_token for device in Device.objects.all()]
    message_title = "Message title"
    message_body = "Message body"
    result = push_service.notify_multiple_devices(registration_ids=registration_ids, message_title=message_title, message_body=message_body)

    status = 'ERROR'
    if result[0]['success'] == 1:
        status = 'OK'

    return JsonResponse({'status': status})
