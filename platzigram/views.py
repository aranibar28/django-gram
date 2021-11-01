from django.http import HttpResponse
from datetime import datetime
import json

def hello_world(request):
    now = datetime.now().strftime('%b %dth %Y - %H:%M hrs')
    return HttpResponse('Hola papu, esta es la hora del servidor: {now}'.format(now=now))

def sorted_integer(request):
    numbers = request.GET['numbers']
    sorted_numbers = sorted(map(int, numbers.split(',')))
    content_type='application/json'

    data = {
        'status': 'success',
        'numbers': sorted_numbers,
        'messages': 'Integers sorted successfully.'
    }

    return HttpResponse(json.dumps(data, indent=4), content_type)

def say_hi(request, name, age):
    
    if age < 12:
        message = 'Sorry {}, you are not allowed here'.format(name)
    else:
        message = 'Hello, {}! Welcome to Platzi'.format(name)

    return HttpResponse(message)
