import json

from django.db.models import F
from django.http import JsonResponse
from django.shortcuts import render
from .te_api import get_correct_data
from .models import Country, Category


# Create your views here.
def index(request):
    return render(request, 'te_demo/index.html')


def get_countries_list(request):
    countries = list(
        Country.objects.all().annotate(Country=F('country')).values('Country')
    )
    return JsonResponse({'country_data': countries}, status=200)


def get_categories_list(request):
    categories = list(
        Category.objects.all().annotate(Category=F('category'), CategoryGroup=F('category_group')).values('Category', 'CategoryGroup')
    )
    return JsonResponse({'category_data': categories}, status=200)


def get_data(request):
    data = dict(request.GET)
    data = {key: value[0] for key, value in zip(data.keys(), data.values()) if value[0]}
    if not data:
        return JsonResponse({'msg': 'NOT_OK'}, status=200)
    print(data)
    df_json, df_columns = get_correct_data(data)
    return JsonResponse({'table_data': df_json, 'column_names': df_columns}, safe=False, status=200)

