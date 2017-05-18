import pathlib
import json

from falcon import errors
import hug

api_path = pathlib.Path('.')
data_path = api_path.joinpath('data')

def load_data(filename):
    with open(data_path.joinpath(filename)) as fp:
        return json.load(fp)

@hug.get('/')
def hello():
    return {
        "Welcome to SRD API"
    }

@hug.get('/race')
def get_race(name: hug.types.text):
    data = load_data('races.json')
    for item in data:
        if item['name'].lower() == name.lower():
            return item
    else:
        raise errors.HTTPBadRequest("Bad Request", "Has no race {}".format(name))
