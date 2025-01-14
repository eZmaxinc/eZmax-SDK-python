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

from eZmaxApi.models.ezsignfoldertype_autocomplete_element_response import EzsignfoldertypeAutocompleteElementResponse

class TestEzsignfoldertypeAutocompleteElementResponse(unittest.TestCase):
    """EzsignfoldertypeAutocompleteElementResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsignfoldertypeAutocompleteElementResponse:
        """Test EzsignfoldertypeAutocompleteElementResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsignfoldertypeAutocompleteElementResponse`
        """
        model = EzsignfoldertypeAutocompleteElementResponse()
        if include_optional:
            return EzsignfoldertypeAutocompleteElementResponse(
                e_ezsignfoldertype_privacylevel = 'User',
                s_ezsignfoldertype_name_x = 'Default',
                pki_ezsignfoldertype_id = 5,
                b_ezsignfoldertype_isactive = True
            )
        else:
            return EzsignfoldertypeAutocompleteElementResponse(
                e_ezsignfoldertype_privacylevel = 'User',
                s_ezsignfoldertype_name_x = 'Default',
                pki_ezsignfoldertype_id = 5,
                b_ezsignfoldertype_isactive = True,
        )
        """

    def testEzsignfoldertypeAutocompleteElementResponse(self):
        """Test EzsignfoldertypeAutocompleteElementResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
