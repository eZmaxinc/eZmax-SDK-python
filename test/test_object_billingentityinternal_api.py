"""
    eZmax API Definition (Full)

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.1.9
    Contact: support-api@ezmax.ca
    Generated by: https://openapi-generator.tech
"""


import unittest

import eZmaxApi
from eZmaxApi.api.object_billingentityinternal_api import ObjectBillingentityinternalApi  # noqa: E501


class TestObjectBillingentityinternalApi(unittest.TestCase):
    """ObjectBillingentityinternalApi unit test stubs"""

    def setUp(self):
        self.api = ObjectBillingentityinternalApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_billingentityinternal_get_autocomplete_v1(self):
        """Test case for billingentityinternal_get_autocomplete_v1

        Retrieve Billingentityinternals and IDs  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()