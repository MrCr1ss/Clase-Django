from datetime import datetime
from django.shortcuts import render
import datetime

# importar para hacer el envio de informacion 
from django.http import HttpResponse
# Create your views here.

# funcion que recibe el objeto request
def display(request):
    return HttpResponse("<h1>Hola Mundo!</h1>")

def displayDateTime(request):
    dt = datetime.datetime.now()
    s = "<b>Fecha y hora actual:</b>" + str(dt)
    return HttpResponse(s)


