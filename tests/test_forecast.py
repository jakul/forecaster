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


class SumamariseForecastTest(TestCase):
    """
    Tests for summarise_forecast function
    """

    @patch('requests.get')
    def test_good_args(self, mock_requests):
        # Check min, max, dates, weathers, etc
        pass
