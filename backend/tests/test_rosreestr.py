import unittest

from backend.parser.rosreestr import get_result_rossreestr


class TestRosReestr(unittest.TestCase):
    def test_kvartira(self):
        # квартира
        r = get_result_rossreestr("63:10:0104004:2238")
        self.assertDictEqual(r, {'property_unique_identidier': '63:10:0104004:2238', 'property_floor_area': '45.3',
                                 'property_name_rosreestr': 'Квартира, Жилое помещение', 'property_level': '2',
                                 'property_address': 'Российская Федерация, Самарская область, г. Чапаевск, '
                                                     'ул.Орджоникидзе, д.5, кв. 24',
                                 'property_name': 'Квартира'})

    def test_zdanie(self):
        r = get_result_rossreestr("63:01:0109006:3387")
        self.assertDictEqual(r, {'property_unique_identidier': '63:01:0109006:3387', 'property_floor_area': '83.5',
                                 'property_name_rosreestr': 'Здание (Нежилое здание, Строение (мойка), год '
                                                            'постройки 1997)', 'property_level': '1',
                                 'property_address': 'Российская Федерация, Самарская область, г. Самара, '
                                                     'Железнодорожный р-н, ул. Владимирская, 56а',
                                 'property_name': 'Нежилое здание'})

    def test_zemlya(self):
        r = get_result_rossreestr("63:17:0310002:194")
        self.assertDictEqual(r, {'property_unique_identidier': '63:17:0310002:194',
                                 'property_address': 'Самарская область, Волжский район, городское поселение '
                                                     'Смышляевка, п.г.т. Смышляевка, переулок Коммунистический, '
                                                     'земельный участок №22',
                                 'property_land_cat': 'Земли населенных пунктов', 'property_name': 'Земельный участок'}
                             )

    def test_zhiloy_dom(self):
        r = get_result_rossreestr("63:17:0310002:207")
        self.assertDictEqual(r, {'property_unique_identidier': '63:17:0310002:207', 'property_floor_area': '82.9',
                                 'property_name_rosreestr': 'Здание (Жилой дом)', 'property_level': '1',
                                 'property_address': 'Самарская область, Волжский район, п.г.т. Смышляевка, '
                                                     'пер. Коммунистический, д. 22',
                                 'property_name': 'Жилой дом'}
                             )


if __name__ == "__main__":
    unittest.main()
