import pandas as pd
import tradingeconomics as te
from example_website import settings

pd.set_option('display.max_rows', 10)

TE_SECRET = settings.TE_SECRET


def te_login():
    res = te.login(TE_SECRET)
    print(res)


def get_comtrade_by_country(country: str, type_selector: str) -> pd.DataFrame:
    te_login()
    df = te.getCmtCountryFilterByType(country1=country.capitalize(), type=type_selector,
                                      output_type='df')  # te.getCmtCountry(output_type='df')
    try:
        if df.empty:
            return df
    except AttributeError:
        return pd.DataFrame()
    df = df.drop(['url', 'symbol', 'lastupdate'], axis=1)
    df = df.drop(df[df['country2'] == 'World'].index)
    return df


def get_formatted_data(data: dict):
    df = get_comtrade_by_country(**data)
    if df.empty:
        return []
    df_columns = df.columns.to_list()
    # unique_column_values = get_unique_col_values(df)
    df_json = df.to_json(orient='records')
    return [df_json, df_columns, df]
