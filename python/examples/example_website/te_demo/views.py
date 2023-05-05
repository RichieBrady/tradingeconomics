import json
import pickle

from django.db.models import F
from django.http import JsonResponse
from django.shortcuts import render
from .te_api import get_formatted_data
from .models import Country, Category
from django.core.cache import cache

from . import dash_app


def index(request):
    return render(request, 'te_demo/index.html')


def get_countries_list(request):
    countries = list(
        Country.objects.all().annotate(Country=F('country')).values('Country')
    )
    return JsonResponse({'country_data': countries}, status=200)


def get_data(request):
    data = dict(request.GET)
    data = {key: value[0] for key, value in zip(data.keys(), data.values()) if value[0]}
    if not data:
        return JsonResponse({'msg': 'NOT_OK'}, status=404)

    if formatted_data := get_formatted_data(data):
        df_json, df_columns, df = formatted_data
        pickled_df = pickle.dumps(df)
        cache.set('my_pickled_df', pickled_df, timeout=3600)
        return JsonResponse({'table_data': df_json, 'column_names': df_columns}, safe=False, status=200)

    return JsonResponse({'msg': 'NOT_OK'}, status=404)

