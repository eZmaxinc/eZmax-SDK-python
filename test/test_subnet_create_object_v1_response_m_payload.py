# coding: utf-8

"""
    eZmax API Definition (Full)

    This API expose all the functionnalities for the eZmax and eZsign applications.

    The version of the OpenAPI document: 1.2.0
    Contact: support-api@ezmax.ca
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from eZmaxApi.models.subnet_create_object_v1_response_m_payload import SubnetCreateObjectV1ResponseMPayload  # noqa: E501

class TestSubnetCreateObjectV1ResponseMPayload(unittest.TestCase):
    """SubnetCreateObjectV1ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SubnetCreateObjectV1ResponseMPayload:
        """Test SubnetCreateObjectV1ResponseMPayload
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SubnetCreateObjectV1ResponseMPayload`
        """
        model = SubnetCreateObjectV1ResponseMPayload()  # noqa: E501
        if include_optional:
            return SubnetCreateObjectV1ResponseMPayload(
                a_pki_subnet_id = [
                    3
                    ]
            )
        else:
            return SubnetCreateObjectV1ResponseMPayload(
                a_pki_subnet_id = [
                    3
                    ],
        )
        """

    def testSubnetCreateObjectV1ResponseMPayload(self):
        """Test SubnetCreateObjectV1ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()