# Welcome to Forecaster.

[![build-status-image]][travis-url]

Forecaster is a script which let's you find out what the weather will be where you are using the [openweathermap.org REST API][openweathermap-rest-api].



# Testing
Forecaster is tested against Python 2.6 and Python 2.7. The only requirement is a version of the [Requests][requests] library. [Tox][tox] is used to run tests against all supported versions of Requests and Python 

[openweathermap-rest-api]: http://openweathermap.org/API
[requests]: http://docs.python-requests.org/en/latest/
[tox]: https://tox.readthedocs.org/en/latest/
[build-status-image]: https://travis-ci.org/jakul/forecaster.svg?branch=master
[travis-url]: https://travis-ci.org/jakul/forecaster