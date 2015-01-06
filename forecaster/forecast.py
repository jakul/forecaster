# coding: utf-8
from collections import defaultdict
import requests
import datetime
from forecaster import ForecasterException

def get_forecast(location, num_days=None, units=None):
    """
    Query the OpenWeatherMap API for the forecast for a given location.

    :param location: Where to find the forecast of
    :param num_days: How many days forecast to return, starting with today.
    Optional. Defaults to 14.
    :param units: `imperial` or `metric`. Optional. Defaults to 'imperial'
    :return: The OWM API response content
    :raises ForecasterException: If there was a problem getting the data from
    the OWM API
    """
    # TODO: cache the result for 10 minutes, as recommend by OWM
    if num_days is None:
        num_days = 14
    if units is None:
        units = 'imperial'

    url = (
        u'http://api.openweathermap.org/data/2.5/forecast/daily?q={location}'
        u'&mode=json&units={units}&cnt={num_days}'.format(**locals())
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
            'OpenWeatherMapAPI returned 200 status code but with no useful '
            'content', response.content, url
        )

    return data

def summarise_forecast(location):
    """

    :param location:
    :return:
    """
    forecast = get_forecast(location)
    summary = {'city': location, 'forecasts': defaultdict(set)}

    # Set the initial min and max to be that of the the first forecast
    summary['min'] = forecast[u'list'][0][u'temp'][u'min']
    summary['max'] = forecast[u'list'][0][u'temp'][u'max']
    for day_forecast in (forecast['list']):
        # Update the min and max temperatures
        summary['min'] = min(day_forecast[u'temp'][u'min'], summary['min'])
        summary['max'] = max(day_forecast[u'temp'][u'max'], summary['max'])
        date = datetime.datetime.fromtimestamp(
            day_forecast[u'dt']
        ).strftime('%Y-%m-%d')
        for weather in day_forecast[u'weather']:
            # Note: There is a unicode to string conversion here, which would
            # cause problems if any of the weather types used non-ascii
            # characters
            summary['forecasts'][str(weather[u'main'])].add(date)

    # Convert the forecasts to the expected output format
    summary['forecasts'] = dict(summary['forecasts'])
    for weather_type, dates in summary['forecasts'].items():
        summary['forecasts'][weather_type] = sorted(list(dates))

    return summary