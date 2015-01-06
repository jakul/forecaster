# Welcome to Forecaster.

[![build-status-image]][travis-url]

Forecaster lets you find out what the weather will be where you are using the [openweathermap.org REST API][openweathermap-rest-api].

# Support
Forecaster depends on [Requests][requests] to run, and [py.test][pytest], [tox][tox] and [mock][mock] for test running. Forecaster runs on Python 2.6 and 2.7.

# How to use
```python
>>> from forecaster import forecast

>>> forecast.summarise_forecast('rio')
{'city': 'rio',
 'forecasts': {u'Clear': ['2015-01-18', '2015-01-06'],
  u'Clouds': ['2015-01-07', '2015-01-08'],
  u'Rain': ['2015-01-19',
   '2015-01-09',
   '2015-01-10',
   '2015-01-11',
   '2015-01-12',
   '2015-01-13',
   '2015-01-14',
   '2015-01-15',
   '2015-01-16',
   '2015-01-17']},
 'max': 84.25,
 'min': 67.21}
 
>>> forecast.get_forecast(u'Águeda', num_days=2, units='metric')
{u'city': {u'coord': {u'lat': 40.5767, u'lon': -8.44933},
  u'country': u'Portugal',
  u'id': u'2743292',
  u'name': u'\xc1gueda',
  u'population': 0},
 u'cnt': 2,
 u'cod': u'200',
 u'list': [{u'clouds': 0,
   u'deg': 87,
   u'dt': 1420545600,
   u'humidity': 95,
   u'pressure': 968.03,
   u'speed': 0.86,
   u'temp': {u'day': -3.57,
    u'eve': -3.57,
    u'max': -3.57,
    u'min': -9.2,
    u'morn': -3.57,
    u'night': -9.2},
   u'weather': [{u'description': u'sky is clear',
     u'icon': u'01n',
     u'id': 800,
     u'main': u'Clear'}]},
  {u'clouds': 0,
   u'deg': 85,
   u'dt': 1420632000,
   u'humidity': 88,
   u'pressure': 971.42,
   u'speed': 1.32,
   u'temp': {u'day': -0.42,
    u'eve': -1.59,
    u'max': 3.32,
    u'min': -9.2,
    u'morn': -9.2,
    u'night': -5.3},
   u'weather': [{u'description': u'sky is clear',
     u'icon': u'01d',
     u'id': 800,
     u'main': u'Clear'}]}],
 u'message': 1.2784}
```

# How to install
Use [pip][pip]!

```
pip install git+https://github.com/jakul/forecaster.git
```

Or to get a specific version

```
pip install git+https://github.com/jakul/forecaster.git@version-0.0.1
```

# Development
Contributions are **welcome**. Please make any code enhancements, bug fixes in a new branch on your own fork of this repo. Make sure to add tests for your changes and then [make a pull request][make-a-pull-request] when you're finished.

## Testing

To run the tests, clone the repository, and then:

    # Setup the virtual environment
    virtualenv env
    env/bin/activate
    pip install -r requirements.txt

    # Run the tests
    py.test

You can also use the excellent [`tox`][tox] testing tool to run the tests against all supported versions of Python.  Install `tox` globally, and then simply run:

    tox




[openweathermap-rest-api]: http://openweathermap.org/API
[requests]: http://docs.python-requests.org/en/latest/
[tox]: https://tox.readthedocs.org/en/latest/
[build-status-image]: https://travis-ci.org/jakul/forecaster.svg?branch=master
[travis-url]: https://travis-ci.org/jakul/forecaster
[pytest]: http://pytest.org/latest/
[mock]: https://pypi.python.org/pypi/mock
[make-a-pull-request]: https://help.github.com/articles/creating-a-pull-request/
[pip]: https://pypi.python.org/pypi/pip