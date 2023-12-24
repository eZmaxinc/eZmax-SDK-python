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

from eZmaxApi.models.ezsigntsarequirement_autocomplete_element_response import EzsigntsarequirementAutocompleteElementResponse

class TestEzsigntsarequirementAutocompleteElementResponse(unittest.TestCase):
    """EzsigntsarequirementAutocompleteElementResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsigntsarequirementAutocompleteElementResponse:
        """Test EzsigntsarequirementAutocompleteElementResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsigntsarequirementAutocompleteElementResponse`
        """
        model = EzsigntsarequirementAutocompleteElementResponse()
        if include_optional:
            return EzsigntsarequirementAutocompleteElementResponse(
                s_ezsigntsarequirement_description_x = 'No',
                pki_ezsigntsarequirement_id = 1,
                b_ezsigntsarequirement_isactive = True,
                b_disabled = True
            )
        else:
            return EzsigntsarequirementAutocompleteElementResponse(
                s_ezsigntsarequirement_description_x = 'No',
                pki_ezsigntsarequirement_id = 1,
                b_ezsigntsarequirement_isactive = True,
                b_disabled = True,
        )
        """

    def testEzsigntsarequirementAutocompleteElementResponse(self):
        """Test EzsigntsarequirementAutocompleteElementResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
