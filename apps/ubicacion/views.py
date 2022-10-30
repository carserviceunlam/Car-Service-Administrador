from django.shortcuts import render
from .models import Ciudad
from django.http import JsonResponse
# Create your views here.
def get_ciudad(_request, id):
    ciudad = Ciudad.objects.filter(id=id).first()

    if (ciudad):
        data = {'message': "Success", 'ciudad': ciudad.province_id.name}
    else:
        data = {'message': "Not Found"}

    return JsonResponse(data)