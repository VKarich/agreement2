from template import Templater
from tables import Tableter


def transform_request(input_json):
    model = input_json["model"]
    model["select_second_step"] = input_json["select_second_step"]
    model["select_third_step"] = input_json["select_third_step"]
    model["payMethod"] = [p['name'] for p in model["payMethod"]]
    return model


def generate_file(input_json):
    model = transform_request(input_json)
    Tableter.generate_file(model)
    Templater.generate_file(model)
    return True
