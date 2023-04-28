import pandas as pd
import tradingeconomics as te
from example_website import settings

from .models import Country, Category

TE_SECRET = settings.TE_SECRET


def te_login():
    res = te.login(TE_SECRET)
    print(res)


def get_country_list():
    te_login()
    df = te.getEurostatData(lists='countries', output_type='df')
    df.rename(columns={'Country': 'country'}, inplace=True)
    data_list = df.to_dict('records')
    models_objects = [Country(country=data['country']) for data in data_list]
    Country.objects.bulk_create(models_objects)


def get_category_list():
    te_login()
    df = te.getEurostatData(lists='categories', output_type='df')
    df.rename(columns={'Category': 'category', 'CategoryGroup': 'category_group'}, inplace=True)
    data_list = df.to_dict('records')
    models_objects = [Category(**data) for data in data_list]
    Category.objects.bulk_create(models_objects)


def get_by_country(country: str) -> pd.DataFrame:
    te_login()
    df = te.getEurostatData(country=country.capitalize(), output_type='df')
    df = df.drop(['ID', 'URL', 'Unit', 'LatestValueDate', 'PreviousValueDate', 'FirstValueDate', 'HighestValueDate', 'LowestValueDate',
                  'LastUpdate'], axis=1)
    return df


def get_by_category(category: str) -> pd.DataFrame:
    te_login()
    df = te.getEurostatData(category=category.capitalize(), output_type='df')
    df = df.drop(['ID', 'URL', 'Unit', 'LatestValueDate', 'PreviousValueDate', 'FirstValueDate', 'HighestValueDate', 'LowestValueDate',
                  'LastUpdate'], axis=1)
    return df


def get_by_category_group(group: str) -> pd.DataFrame:
    te_login()
    df = te.getEurostatData(category_group=group.capitalize(), output_type='df')
    df = df.drop(['ID', 'URL', 'Unit', 'LatestValueDate', 'PreviousValueDate', 'FirstValueDate', 'HighestValueDate', 'LowestValueDate',
                  'LastUpdate'], axis=1)
    return df


def get_by_country_and_category(country: str, category: str) -> pd.DataFrame:
    te_login()
    print(country, category)
    df = te.getEurostatData(country=country.capitalize(), category=category.capitalize(), output_type='df')
    df = df.drop(['ID', 'URL', 'Unit', 'LatestValueDate', 'PreviousValueDate', 'FirstValueDate', 'HighestValueDate', 'LowestValueDate',
                  'LastUpdate'], axis=1)
    return df


def get_by_country_and_category_group(country: str, category_group: str) -> pd.DataFrame:
    te_login()
    df = te.getEurostatData(country=country.capitalize(), category_group=category_group.capitalize(), output_type='df')
    df = df.drop(['ID', 'URL', 'Unit', 'LatestValueDate', 'PreviousValueDate', 'FirstValueDate', 'HighestValueDate', 'LowestValueDate',
                  'LastUpdate'], axis=1)
    return df


def get_single_param_data(param: dict) -> pd.DataFrame:
    if country := param.get('country'):
        return get_by_country(country)
    elif category := param.get('category'):
        return get_by_category(category)
    elif category_group := param.get('category_group'):
        return get_by_category_group(category_group)


def get_double_param_data(params: dict) -> pd.DataFrame:
    country = params.get('country')
    if category := params.get('category'):
        return get_by_country_and_category(country, category)
    elif category_group := params.get('category_group'):
        return get_by_country_and_category_group(country, category_group)


def get_correct_data(data: dict):
    df_json = None
    df_columns = None
    if len(data) == 1:
        df = get_single_param_data(data)
        df_columns = df.columns.to_list()
        df_json = df.to_json(orient='records')
    elif len(data) == 2:
        df = get_double_param_data(data)
        df_columns = df.columns.to_list()
        df_json = df.to_json(orient='records')
    return [df_json, df_columns]
