import tradingeconomics as te
import numpy as np
import pandas as pd

from example_website import settings

TE_SECRET = settings.TE_SECRET


def te_login():
    res = te.login(TE_SECRET)
    print(res)


def get_country_list():
    te_login()
    df = te.getEurostatData(lists='countries', output_type='df')
    print(df.head())
    print(df.describe())


def get_category_list():
    te_login()
    df = te.getEurostatData(lists='categories', output_type='df')
    print(df.head())
    print(df.describe())


def get_by_category_group(group: str):
    df = te.getEurostatData(category_group=group.capitalize(), output_type='df')
    print(df.head())
    print(df.describe())


def get_by_category(category: str):
    df = te.getEurostatData(category=category.capitalize(), output_type='df')
    print(df.head())
    print(df.describe())


def get_by_country(country: str):
    df = te.getEurostatData(country=country.capitalize(), output_type='df')
    print(df.head())
    print(df.describe())


def get_by_country_and_category(country: str, category: str):
    df = te.getEurostatData(country=country.capitalize(), category=category.capitalize(), output_type='df')
    print(df.head())
    print(df.describe())


def get_by_country_and_category_group(country: str, category_group: str):
    df = te.getEurostatData(country=country.capitalize(), category_group=category_group.capitalize(), output_type='df')
    print(df.head())
    print(df.describe())
