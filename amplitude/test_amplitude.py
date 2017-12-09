import unittest
import sys
import requests_mock
from requests_mock.contrib import fixture
import testtools

sys.path.insert(0,"..")
import amplitude

class AmplitudeLoggerTest(testtools.TestCase):

    AMPLITUDE_API_KEY = "someapikey"
    AMPLITUDE_API_URI = "https://api.amplitude.com/httpapi"
    AMPLITUDE_TEST_RESPONSE = "APIok"

    def setUp(self):
        super(AmplitudeLoggerTest, self).setUp()
        self.requests_mock = self.useFixture(fixture.Fixture())
        self.amplitude_logger = amplitude.AmplitudeLogger(api_key=self.AMPLITUDE_API_KEY, 
                                                          api_uri=self.AMPLITUDE_API_URI)

    def test_log_event(self):
        self.requests_mock.register_uri('POST', self.AMPLITUDE_API_URI, text=self.AMPLITUDE_TEST_RESPONSE)
        event_args = {"device_id":"devid", "event_type":"testingtesting", "event_properties":{"foo":"bar", "zoo":"sofa"}}
        event = self.amplitude_logger.create_event(**event_args)
        result = self.amplitude_logger.log_event(event)
        assert result.text == self.AMPLITUDE_TEST_RESPONSE

if __name__ == "__main__":
    testtools.main()
