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

from eZmaxApi.models.franchisebroker_autocomplete_element_response import FranchisebrokerAutocompleteElementResponse

class TestFranchisebrokerAutocompleteElementResponse(unittest.TestCase):
    """FranchisebrokerAutocompleteElementResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FranchisebrokerAutocompleteElementResponse:
        """Test FranchisebrokerAutocompleteElementResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FranchisebrokerAutocompleteElementResponse`
        """
        model = FranchisebrokerAutocompleteElementResponse()
        if include_optional:
            return FranchisebrokerAutocompleteElementResponse(
                s_franchisebroker_name = 'Default',
                pki_franchisebroker_id = 61,
                b_franchisebroker_isactive = True
            )
        else:
            return FranchisebrokerAutocompleteElementResponse(
                s_franchisebroker_name = 'Default',
                pki_franchisebroker_id = 61,
                b_franchisebroker_isactive = True,
        )
        """

    def testFranchisebrokerAutocompleteElementResponse(self):
        """Test FranchisebrokerAutocompleteElementResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
