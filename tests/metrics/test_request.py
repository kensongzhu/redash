from mock import patch, ANY
from tests import BaseTestCase


@patch("statsd.StatsClient.timing")
class TestRequestMetrics(BaseTestCase):
    def test_flask_request_records_statsd_metrics(self, timing):
        self.client.get("{}/ping".format(self.app.config["REDASH_APPLICATION_ROOT"]))
        timing.assert_called_once_with("requests.redash_ping.get", ANY)
