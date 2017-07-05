from django.http import JsonResponse

from .models import Device


def api_register(request):
    if request.GET.get('id'):
        device = Device.objects.get(id=request.GET['id'])
        if request.GET.get('firebase_token'):
            device.firebase_token = request.GET['firebase_token']
        device.save()
    else:
        device = Device()
        device.name = request.GET.get('name')
        device.save()
    return JsonResponse({'id': device.id})
