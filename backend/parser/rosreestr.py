import pandas as panda
import logging

URL = r'https://rosreestr.gov.ru/wps/portal/p/cc_ib_portal_services/online_request/!ut/p/z1/pVBNT8MwDP0tHDjHafd9C9s' \
      r'00GBjX7D2EqVZtGVq0ypNQfx7nLZiXNgORD7E9nvPzyYx2ZPYiA99FE7nRqSYR3GPz1adKR136Hy2on1gT2xOQzoD2HbJ-1XAkpL4P3wEeD' \
      r'788RggP746YhzcAHiLt4ZEaLLPgT4yyjrBfDnZDoGtQ3h7XgQBACUbryFz42yepsqS6B42Slh5YtIf0ndPeVUqVMJvnh64qbLEA31eOquU-' \
      r'_lX0lW2hYpCWJcp03alqJkk6oUjoBgwBOiNwnDQvwhx91UgHRNoiijBi7zUtZWoO_RVq48nx606tmOr5KxkOyWpdHrQpm0hpubVMOVcqi5-' \
      r'ynpJLpotI_Su6gWTc2PzF6YxNWYTvti9PEzXvqWMxDNYYaRqrRTZbg_6NcsG4R_xefcNhLgymg!!/p0/IZ7_01HA1A42KODT90AR30VLN22' \
      r'001=CZ6_GQ4E1C41KGQ170AIAK131G00T5=MEcontroller!QCPObjectDataController==/?object_data_id={object_id}&' \
      r'dbName=firLite&region_key=163'

logger = logging.getLogger(__name__)


def get_result_rossreestr(object_id: str):
    tables = panda.read_html(URL.format(object_id=object_id), encoding='utf-8', decimal=',', thousands='.')
    t = tables[2]
    t.columns = ['key_', 'value_']
    t.set_index('key_', inplace=True)
    data = t.to_dict()['value_']
    # property_name
    attrs = {"Кадастровый номер:": "property_unique_identidier",
             "Площадь ОКС'a:": "property_floor_area",
             "(ОКС) Тип:": "property_name_rosreestr",
             "(ОКС) Этажность:": "property_level",
             "Этаж:": "property_level",
             "Адрес (местоположение):": "property_address",
             "Категория земель:": "property_land_cat"
             }

    result = {}
    for k, v in attrs.items():
        if k in data:
            result[v] = data[k]

    if 'property_land_cat' in result:
        result['property_name'] = 'Земельный участок'
    elif result['property_name_rosreestr'].startswith('Квартира'):
        result['property_name'] = 'Квартира'
    elif result['property_name_rosreestr'].startswith('Здание (Нежилое здание'):
        result['property_name'] = 'Нежилое здание'
    elif result['property_name_rosreestr'].startswith('Здание (Жилой дом'):
        result['property_name'] = 'Жилой дом'

    return result
