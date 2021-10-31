# Django
from django.http import HttpResponse
# Utilities
from datetime import datetime

def hello_world(request):
    now = datetime.now().strftime('%b %dth %Y - %H:%M hrs')
    return HttpResponse('Hola papu, esta es la hora del servidor: {now}'.format(now=now))

def hi(request):
    # import pdb; pdb.set_trace()
    return HttpResponse("Holaa !!!")