import json
import os

from dotenv import load_dotenv
from six import PY3

from solarwinds import do_query

load_dotenv()
QUERY_URL = 'https://%s:17778/SolarWinds/InformationService/v3/Json/Query' % os.getenv('ORION_SERVER')


def test_do_query(requests_mock):
    requests_mock.post(QUERY_URL, text=read_file('example_data.json'))
    result = do_query("SELECT ServerName FROM Orion.Engines")
    assert result == 'some results'


def read_file(filename):
    with open(get_path_to_file(filename), "r") as f:
        return f.read() if PY3 else f.read().decode("utf-8")


def load_json_from_file(filename):
    raw_json_file = read_file(filename)
    return json.loads(raw_json_file)


def get_path_to_file(filename):
    path_to_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'samples', filename)
    return path_to_file
