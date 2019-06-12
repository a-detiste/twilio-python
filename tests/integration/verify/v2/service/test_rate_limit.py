# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base.exceptions import TwilioException
from twilio.http.response import Response


class RateLimitTestCase(IntegrationTestCase):

    def test_create_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.verify.v2.services(sid="VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .rate_limits.create(unique_name="unique_name")

        values = {'UniqueName': "unique_name", }

        self.holodeck.assert_has_request(Request(
            'post',
            'https://verify.twilio.com/v2/Services/VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/RateLimits',
            data=values,
        ))

    def test_create_rate_limit_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "sid": "RKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "service_sid": "VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "unique_name": "unique.name",
                "description": "Description",
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "url": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/RateLimits/RKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "links": {
                    "buckets": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/RateLimits/RKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Buckets"
                }
            }
            '''
        ))

        actual = self.client.verify.v2.services(sid="VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .rate_limits.create(unique_name="unique_name")

        self.assertIsNotNone(actual)

    def test_update_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.verify.v2.services(sid="VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .rate_limits(sid="RKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update()

        self.holodeck.assert_has_request(Request(
            'post',
            'https://verify.twilio.com/v2/Services/VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/RateLimits/RKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_update_rate_limit_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "sid": "RKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "service_sid": "VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "unique_name": "unique.name",
                "description": "Description",
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "url": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/RateLimits/RKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "links": {
                    "buckets": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/RateLimits/RKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Buckets"
                }
            }
            '''
        ))

        actual = self.client.verify.v2.services(sid="VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .rate_limits(sid="RKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update()

        self.assertIsNotNone(actual)

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.verify.v2.services(sid="VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .rate_limits(sid="RKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://verify.twilio.com/v2/Services/VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/RateLimits/RKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_fetch_rate_limit_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "sid": "RKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "service_sid": "VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "unique_name": "unique.name",
                "description": "Description",
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "url": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/RateLimits/RKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "links": {
                    "buckets": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/RateLimits/RKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Buckets"
                }
            }
            '''
        ))

        actual = self.client.verify.v2.services(sid="VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .rate_limits(sid="RKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.assertIsNotNone(actual)

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.verify.v2.services(sid="VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .rate_limits.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://verify.twilio.com/v2/Services/VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/RateLimits',
        ))

    def test_read_all_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "meta": {
                    "page": 0,
                    "page_size": 50,
                    "first_page_url": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/RateLimits?PageSize=50&Page=0",
                    "previous_page_url": null,
                    "next_page_url": null,
                    "key": "rate_limits",
                    "url": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/RateLimits?PageSize=50&Page=0"
                },
                "rate_limits": [
                    {
                        "sid": "RKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "service_sid": "VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "unique_name": "unique.name",
                        "description": "Description",
                        "date_created": "2015-07-30T20:00:00Z",
                        "date_updated": "2015-07-30T20:00:00Z",
                        "url": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/RateLimits/RKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "links": {
                            "buckets": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/RateLimits/RKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Buckets"
                        }
                    }
                ]
            }
            '''
        ))

        actual = self.client.verify.v2.services(sid="VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .rate_limits.list()

        self.assertIsNotNone(actual)

    def test_delete_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.verify.v2.services(sid="VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .rate_limits(sid="RKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").delete()

        self.holodeck.assert_has_request(Request(
            'delete',
            'https://verify.twilio.com/v2/Services/VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/RateLimits/RKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_delete_response(self):
        self.holodeck.mock(Response(
            204,
            None,
        ))

        actual = self.client.verify.v2.services(sid="VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .rate_limits(sid="RKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").delete()

        self.assertTrue(actual)