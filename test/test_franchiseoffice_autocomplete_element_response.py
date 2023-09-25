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

from eZmaxApi.models.franchiseoffice_autocomplete_element_response import FranchiseofficeAutocompleteElementResponse  # noqa: E501

class TestFranchiseofficeAutocompleteElementResponse(unittest.TestCase):
    """FranchiseofficeAutocompleteElementResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FranchiseofficeAutocompleteElementResponse:
        """Test FranchiseofficeAutocompleteElementResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FranchiseofficeAutocompleteElementResponse`
        """
        model = FranchiseofficeAutocompleteElementResponse()  # noqa: E501
        if include_optional:
            return FranchiseofficeAutocompleteElementResponse(
                s_franchiseoffice_description = 'Default',
                pki_franchiseoffice_id = 50,
                b_franchiseoffice_isactive = True
            )
        else:
            return FranchiseofficeAutocompleteElementResponse(
                s_franchiseoffice_description = 'Default',
                pki_franchiseoffice_id = 50,
                b_franchiseoffice_isactive = True,
        )
        """

    def testFranchiseofficeAutocompleteElementResponse(self):
        """Test FranchiseofficeAutocompleteElementResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
