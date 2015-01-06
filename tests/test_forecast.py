# coding: utf-8
from unittest import TestCase
from mock import patch, Mock, MagicMock
from forecaster import forecast, ForecasterException
import pytest


class GetForecastTest(TestCase):
    """
    Tests for get_forecast function
    """
    valid_content = {'cod': '200'}
    unknown_place_content = {'cod': '404'}

    @classmethod
    def _valid_response(*args, **kwargs):
        response = Mock()
        response.status_code = 200
        response.content = GetForecastTest.valid_content
        response.json = Mock(return_value=GetForecastTest.valid_content)
        return response

    @patch('requests.get')
    def test_get_forecast(self, mock_requests):
        # Do some setup
        mock_requests.side_effect = GetForecastTest._valid_response

        # Run the code
        data = forecast.get_forecast('Berlin')

        # Check the response
        assert data, GetForecastTest.valid_content

    @patch('requests.get')
    def test_non_ascii_place_name(self, mock_requests):
        # Do some setup
        mock_requests.side_effect = GetForecastTest._valid_response

        # Run the code
        data = forecast.get_forecast(u'Águeda')

        # Check the response
        assert data, GetForecastTest.valid_content

    @patch('requests.get')
    def test_num_days(self, mock_requests):
        # Do some setup
        def side_effect(*args, **kwargs):
            assert 'cnt=7' in args[0]
            return GetForecastTest._valid_response(*args, **kwargs)

        mock_requests.side_effect = side_effect

        # Run the code
        forecast.get_forecast('anywhere', num_days=7)

    @patch('requests.get')
    def test_units(self, mock_requests):
        # Do some setup
        def side_effect(*args, **kwargs):
            assert 'units=metric' in args[0]
            return GetForecastTest._valid_response(*args, **kwargs)

        mock_requests.side_effect = side_effect

        # Run the code
        forecast.get_forecast('anywhere', units='metric')

    @patch('requests.get')
    def test_non_200_status_code(self, mock_requests):
        # Do some setup
        def side_effect(*args, **kwargs):
            response = Mock()
            response.status_code = 404
            return response

        mock_requests.side_effect = side_effect

        # Run the code
        with pytest.raises(ForecasterException) as excinfo:
            forecast.get_forecast('anywhere')

        # Check the error message
        expected_error = 'OpenWeatherMapAPI returned non-200 status code'
        assert excinfo.value[0] == expected_error

    @patch('requests.get')
    def test_not_json(self, mock_requests):
        # Do some setup
        def side_effect(*args, **kwargs):
            response = Mock()
            response.status_code = 200
            response.content = 'not json'
            response.json = Mock(side_effect=ValueError)
            return response

        mock_requests.side_effect = side_effect

        # Run the code
        with pytest.raises(ForecasterException) as excinfo:
            forecast.get_forecast('anywhere')

        # Check the error message
        assert excinfo.value[0] == 'Could not decode json'

    @patch('requests.get')
    def test_unknown_place(self, mock_requests):
        # Do some setup
        def side_effect(*args, **kwargs):
            response = Mock()
            response.status_code = 200
            response.content = 'not json'
            response.json = Mock(side_effect=ValueError)
            response.content = GetForecastTest.unknown_place_content
            response.json = Mock(return_value=GetForecastTest.unknown_place_content)
            return response

        mock_requests.side_effect = side_effect

        # Run the code
        with pytest.raises(ForecasterException) as excinfo:
            forecast.get_forecast('anywhere')

        # Check the error message
        expected_error = (
            'OpenWeatherMapAPI returned 200 status code but with no useful '
            'content'
        )
        assert excinfo.value[0] == expected_error


class SummariseForecastTest(TestCase):
    """
    Tests for summarise_forecast function
    """
    valid_content = {u'city': {u'coord': {u'lat': 38.716671, u'lon': -9.13333},
      u'country': u'PT',
      u'id': 2267057,
      u'name': u'Lisbon',
      u'population': 0,
      u'sys': {u'population': 0}},
     u'cnt': 14,
     u'cod': u'200',
     u'list': [{u'clouds': 48,
       u'deg': 153,
       u'dt': 1420545600,
       u'humidity': 100,
       u'pressure': 1041.17,
       u'speed': 6.72,
       u'temp': {u'day': 55,
        u'eve': 55,
        u'max': 55.44,
        u'min': 55,
        u'morn': 55,
        u'night': 55.44},
       u'weather': [{u'description': u'scattered clouds',
         u'icon': u'03n',
         u'id': 802,
         u'main': u'Clouds'}]},
      {u'clouds': 0,
       u'deg': 75,
       u'dt': 1420632000,
       u'humidity': 100,
       u'pressure': 1044.38,
       u'speed': 9.12,
       u'temp': {u'day': 52.29,
        u'eve': 53.44,
        u'max': 54.97,
        u'min': 52.09,
        u'morn': 54.97,
        u'night': 54.21},
       u'weather': [{u'description': u'sky is clear',
         u'icon': u'01d',
         u'id': 800,
         u'main': u'Clear'}]},
      {u'clouds': 0,
       u'deg': 46,
       u'dt': 1420718400,
       u'humidity': 100,
       u'pressure': 1051.38,
       u'speed': 10.78,
       u'temp': {u'day': 53.37,
        u'eve': 57.15,
        u'max': 57.25,
        u'min': 53.37,
        u'morn': 53.73,
        u'night': 56.89},
       u'weather': [{u'description': u'sky is clear',
         u'icon': u'01d',
         u'id': 800,
         u'main': u'Clear'}]},
      {u'clouds': 0,
       u'deg': 92,
       u'dt': 1420804800,
       u'humidity': 100,
       u'pressure': 1055.24,
       u'speed': 12.25,
       u'temp': {u'day': 55.58,
        u'eve': 58.96,
        u'max': 59.94,
        u'min': 55.42,
        u'morn': 56.23,
        u'night': 59.04},
       u'weather': [{u'description': u'sky is clear',
         u'icon': u'01d',
         u'id': 800,
         u'main': u'Clear'}]},
      {u'clouds': 0,
       u'deg': 105,
       u'dt': 1420891200,
       u'humidity': 100,
       u'pressure': 1052.03,
       u'speed': 6.96,
       u'temp': {u'day': 56.59,
        u'eve': 57.11,
        u'max': 57.63,
        u'min': 56.48,
        u'morn': 56.88,
        u'night': 57.47},
       u'weather': [{u'description': u'sky is clear',
         u'icon': u'01d',
         u'id': 800,
         u'main': u'Clear'}]},
      {u'clouds': 14,
       u'deg': 23,
       u'dt': 1420977600,
       u'humidity': 0,
       u'pressure': 1050.96,
       u'speed': 14.9,
       u'temp': {u'day': 59.99,
        u'eve': 60.64,
        u'max': 60.71,
        u'min': 59.99,
        u'morn': 60.01,
        u'night': 60.71},
       u'weather': [{u'description': u'sky is clear',
         u'icon': u'01d',
         u'id': 800,
         u'main': u'Clear'}]},
      {u'clouds': 23,
       u'deg': 176,
       u'dt': 1421064000,
       u'humidity': 0,
       u'pressure': 1049.79,
       u'speed': 6.57,
       u'temp': {u'day': 60.78,
        u'eve': 60.15,
        u'max': 60.78,
        u'min': 59.27,
        u'morn': 60.37,
        u'night': 59.27},
       u'weather': [{u'description': u'light rain',
         u'icon': u'10d',
         u'id': 500,
         u'main': u'Rain'}]},
      {u'clouds': 48,
       u'deg': 308,
       u'dt': 1421150400,
       u'humidity': 0,
       u'pressure': 1045.19,
       u'rain': 0.31,
       u'speed': 8.42,
       u'temp': {u'day': 59.34,
        u'eve': 59.13,
        u'max': 59.34,
        u'min': 58.82,
        u'morn': 59.04,
        u'night': 58.82},
       u'weather': [{u'description': u'light rain',
         u'icon': u'10d',
         u'id': 500,
         u'main': u'Rain'}]},
      {u'clouds': 58,
       u'deg': 282,
       u'dt': 1421236800,
       u'humidity': 0,
       u'pressure': 1042.55,
       u'rain': 1.84,
       u'speed': 9.05,
       u'temp': {u'day': 60.15,
        u'eve': 60.22,
        u'max': 60.22,
        u'min': 59.59,
        u'morn': 59.59,
        u'night': 59.85},
       u'weather': [{u'description': u'light rain',
         u'icon': u'10d',
         u'id': 500,
         u'main': u'Rain'}]},
      {u'clouds': 53,
       u'deg': 34,
       u'dt': 1421323200,
       u'humidity': 0,
       u'pressure': 1044.09,
       u'rain': 0.38,
       u'speed': 7.88,
       u'temp': {u'day': 58.62,
        u'eve': 59.32,
        u'max': 59.41,
        u'min': 58.62,
        u'morn': 58.77,
        u'night': 59.41},
       u'weather': [{u'description': u'light rain',
         u'icon': u'10d',
         u'id': 500,
         u'main': u'Rain'}]},
      {u'clouds': 6,
       u'deg': 2,
       u'dt': 1421409600,
       u'humidity': 0,
       u'pressure': 1045.61,
       u'speed': 15.57,
       u'temp': {u'day': 59.23,
        u'eve': 59.56,
        u'max': 59.56,
        u'min': 58.96,
        u'morn': 59.23,
        u'night': 58.96},
       u'weather': [{u'description': u'sky is clear',
         u'icon': u'01d',
         u'id': 800,
         u'main': u'Clear'}]},
      {u'clouds': 34,
       u'deg': 1,
       u'dt': 1421496000,
       u'humidity': 0,
       u'pressure': 1045.82,
       u'speed': 21.56,
       u'temp': {u'day': 59.99,
        u'eve': 59.95,
        u'max': 60.44,
        u'min': 58.95,
        u'morn': 58.95,
        u'night': 60.44},
       u'weather': [{u'description': u'light rain',
         u'icon': u'10d',
         u'id': 500,
         u'main': u'Rain'}]},
      {u'clouds': 0,
       u'deg': 7,
       u'dt': 1421582400,
       u'humidity': 0,
       u'pressure': 1048.35,
       u'speed': 22.18,
       u'temp': {u'day': 60.51,
        u'eve': 61.03,
        u'max': 61.03,
        u'min': 59.68,
        u'morn': 59.68,
        u'night': 60.35},
       u'weather': [{u'description': u'sky is clear',
         u'icon': u'01d',
         u'id': 800,
         u'main': u'Clear'}]},
      {u'clouds': 0,
       u'deg': 4,
       u'dt': 1421668800,
       u'humidity': 0,
       u'pressure': 1047.97,
       u'speed': 14.86,
       u'temp': {u'day': 60.75,
        u'eve': 60.21,
        u'max': 60.75,
        u'min': 60.12,
        u'morn': 60.69,
        u'night': 60.12},
       u'weather': [{u'description': u'sky is clear',
         u'icon': u'01d',
         u'id': 800,
         u'main': u'Clear'}]}],
     u'message': 0.0145}
    multiple_weathers_in_a_day = {u'city': {u'coord': {u'lat': 40.4165, u'lon': -3.70256},
      u'country': u'ES',
      u'id': 3117735,
      u'name': u'Madrid',
      u'population': 0,
      u'sys': {u'population': 0}},
     u'cnt': 1,
     u'cod': u'200',
     u'list': [{u'clouds': 24,
       u'deg': 298,
       u'dt': 1420545600,
       u'humidity': 74,
       u'pressure': 965.54,
       u'speed': 2.72,
       u'temp': {u'day': 26.26,
        u'eve': 26.26,
        u'max': 26.26,
        u'min': 24.15,
        u'morn': 26.26,
        u'night': 24.15},
       u'weather': [{u'description': u'few clouds',
         u'icon': u'02n',
         u'id': 801,
         u'main': u'Clouds'},
        {u'description': u'light rain',
         u'icon': u'10d',
         u'id': 500,
         u'main': u'Rain'}]}],
     u'message': 0.0126}

    @patch('requests.get')
    def test_summarise_forecast(self, mock_requests):
        # Do some setup
        def side_effect(*args, **kwargs):
            response = Mock()
            response.status_code = 200
            response.content = SummariseForecastTest.valid_content
            response.json = Mock(
                return_value=SummariseForecastTest.valid_content
            )
            return response

        mock_requests.side_effect = side_effect

        # Run the code
        summary = forecast.summarise_forecast('Lisbon')

        # Check the response
        expected_summary = {
            'city': 'Lisbon', 'max': 61.03, 'min': 52.09,
            'forecasts': {
                'Clouds': ['2015-01-06'],
                'Clear': [
                    '2015-01-07', '2015-01-08', '2015-01-09','2015-01-10',
                    '2015-01-11', '2015-01-16', '2015-01-18', '2015-01-19'
                ],
                'Rain': [
                    '2015-01-12', '2015-01-13', '2015-01-14', '2015-01-15',
                    '2015-01-17'
                ]
            }
        }

        assert summary==expected_summary

    @patch('requests.get')
    def test_multiple_weathers(self, mock_requests):
        # Do some setup
        def side_effect(*args, **kwargs):
            response = Mock()
            response.status_code = 200
            response.content = SummariseForecastTest.multiple_weathers_in_a_day
            response.json = Mock(
                return_value=SummariseForecastTest.multiple_weathers_in_a_day
            )
            return response

        mock_requests.side_effect = side_effect

        # Run the code
        summary = forecast.summarise_forecast('Madrid')

        # Check the response
        expected_summary = {
            'city': 'Madrid', 'max': 26.26, 'min': 24.15,
            'forecasts': {
                'Clouds': ['2015-01-06'],
                'Rain': ['2015-01-06']
            }
        }

        assert summary==expected_summary
