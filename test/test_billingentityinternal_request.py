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

from eZmaxApi.models.billingentityinternal_request import BillingentityinternalRequest  # noqa: E501

class TestBillingentityinternalRequest(unittest.TestCase):
    """BillingentityinternalRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BillingentityinternalRequest:
        """Test BillingentityinternalRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BillingentityinternalRequest`
        """
        model = BillingentityinternalRequest()  # noqa: E501
        if include_optional:
            return BillingentityinternalRequest(
                pki_billingentityinternal_id = 1,
                obj_billingentityinternal_description = eZmaxApi.models.multilingual_billingentityinternal_description.Multilingual-BillingentityinternalDescription(
                    s_billingentityinternal_description1 = 'Défaut', 
                    s_billingentityinternal_description2 = 'Default', )
            )
        else:
            return BillingentityinternalRequest(
                obj_billingentityinternal_description = eZmaxApi.models.multilingual_billingentityinternal_description.Multilingual-BillingentityinternalDescription(
                    s_billingentityinternal_description1 = 'Défaut', 
                    s_billingentityinternal_description2 = 'Default', ),
        )
        """

    def testBillingentityinternalRequest(self):
        """Test BillingentityinternalRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
