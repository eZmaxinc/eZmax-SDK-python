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

from eZmaxApi.models.ezmaxinvoicing_autocomplete_element_response import EzmaxinvoicingAutocompleteElementResponse  # noqa: E501

class TestEzmaxinvoicingAutocompleteElementResponse(unittest.TestCase):
    """EzmaxinvoicingAutocompleteElementResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzmaxinvoicingAutocompleteElementResponse:
        """Test EzmaxinvoicingAutocompleteElementResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzmaxinvoicingAutocompleteElementResponse`
        """
        model = EzmaxinvoicingAutocompleteElementResponse()  # noqa: E501
        if include_optional:
            return EzmaxinvoicingAutocompleteElementResponse(
                yyyymm_ezmaxinvoicing = '2022-01',
                pki_ezmaxinvoicing_id = 28,
                b_ezmaxinvoicing_isactive = True
            )
        else:
            return EzmaxinvoicingAutocompleteElementResponse(
                yyyymm_ezmaxinvoicing = '2022-01',
                pki_ezmaxinvoicing_id = 28,
                b_ezmaxinvoicing_isactive = True,
        )
        """

    def testEzmaxinvoicingAutocompleteElementResponse(self):
        """Test EzmaxinvoicingAutocompleteElementResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
