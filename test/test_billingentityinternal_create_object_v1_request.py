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

from eZmaxApi.models.billingentityinternal_create_object_v1_request import BillingentityinternalCreateObjectV1Request  # noqa: E501

class TestBillingentityinternalCreateObjectV1Request(unittest.TestCase):
    """BillingentityinternalCreateObjectV1Request unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BillingentityinternalCreateObjectV1Request:
        """Test BillingentityinternalCreateObjectV1Request
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BillingentityinternalCreateObjectV1Request`
        """
        model = BillingentityinternalCreateObjectV1Request()  # noqa: E501
        if include_optional:
            return BillingentityinternalCreateObjectV1Request(
                a_obj_billingentityinternal = [
                    eZmaxApi.models.billingentityinternal_request_compound.billingentityinternal-RequestCompound()
                    ]
            )
        else:
            return BillingentityinternalCreateObjectV1Request(
                a_obj_billingentityinternal = [
                    eZmaxApi.models.billingentityinternal_request_compound.billingentityinternal-RequestCompound()
                    ],
        )
        """

    def testBillingentityinternalCreateObjectV1Request(self):
        """Test BillingentityinternalCreateObjectV1Request"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
