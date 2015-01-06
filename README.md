# Welcome to Forecaster.

[![build-status-image]][travis-url]

Forecaster is a script which let's you find out what the weather will be where you are using the [openweathermap.org REST API][openweathermap-rest-api].

# Support
Forecaster depends on [PyOWM][pyowm] to run, and [py.test][pytest] , [tox][tox] and [mock][mock] for test running. Forecaster runs on Python 2.6 and 2.7.

# How to use

# How to install
Use [pip][pip]!

```
pip install https://github.com/jakul/forecaster/archive/master.zip
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
[pyown]: https://github.com/csparpa/pyowm
[pytest]: http://pytest.org/latest/
[mock]: https://pypi.python.org/pypi/mock
[make-a-pull-request]: https://help.github.com/articles/creating-a-pull-request/
[pip]: https://pypi.python.org/pypi/pip