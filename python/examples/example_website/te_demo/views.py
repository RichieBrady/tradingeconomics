from django.http import JsonResponse
from django.shortcuts import render
from .te_api import te_login


# Create your views here.
def index(request):
    return render(request, 'te_demo/index.html')


def get_data(request):
    data = dict(request.GET)
    te_login()
    print(data)
    return JsonResponse({'msg': 'OK'}, status=200)
