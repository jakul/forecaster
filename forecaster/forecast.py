# coding: utf-8
import requests
from forecaster import ForecasterException

def get_forecast(location, num_days=None, mode=None, units=None):
    # TODO: cache the result for 10 minutes, as recommend by OWM
    if num_days is None:
        num_days = 14
    if mode is None:
        mode = 'json'
    if units is None:
        units = 'imperial'

    #TODO: url escape place name? what about place names with non-ascii chars in them? e.g. Águeda

    url = (
        u'http://api.openweathermap.org/data/2222.5/forecast/daily?q={location}'
        u'&mode={mode}&units={units}&cnt={num_days}'.format(**locals())
    )

    response = requests.get(url)
    if response.status_code != 200:
        raise ForecasterException(
            'OpenWeatherMapAPI returned non-200 status code',
            response.status_code, response.content, url
        )

    # Process data
    try:
        data = response.json()
    except ValueError:
        raise ForecasterException(
            'Could not decode json',
            response.status_code, response.content, url
        )

    # Open Weather Map returns a 200 response even if they can't find the
    # location asked for
    if 'cod' not in data or data['cod'] != '200':
        raise ForecasterException(
            'OpenWeatherMapAPI returned 200 status code but with no content',
            response.content, url
        )

    return data

if __name__ == '__main__':
    get_forecast(u'Águeda')