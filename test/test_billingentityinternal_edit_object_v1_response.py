# coding: utf-8

"""
    eZmax API Definition (Full)

    This API expose all the functionnalities for the eZmax and eZsign applications.

    The version of the OpenAPI document: 1.2.1
    Contact: support-api@ezmax.ca
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from eZmaxApi.models.billingentityinternal_edit_object_v1_response import BillingentityinternalEditObjectV1Response

class TestBillingentityinternalEditObjectV1Response(unittest.TestCase):
    """BillingentityinternalEditObjectV1Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BillingentityinternalEditObjectV1Response:
        """Test BillingentityinternalEditObjectV1Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BillingentityinternalEditObjectV1Response`
        """
        model = BillingentityinternalEditObjectV1Response()
        if include_optional:
            return BillingentityinternalEditObjectV1Response(
            )
        else:
            return BillingentityinternalEditObjectV1Response(
        )
        """

    def testBillingentityinternalEditObjectV1Response(self):
        """Test BillingentityinternalEditObjectV1Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
