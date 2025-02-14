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

from eZmaxApi.models.supply_autocomplete_element_response import SupplyAutocompleteElementResponse

class TestSupplyAutocompleteElementResponse(unittest.TestCase):
    """SupplyAutocompleteElementResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SupplyAutocompleteElementResponse:
        """Test SupplyAutocompleteElementResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SupplyAutocompleteElementResponse`
        """
        model = SupplyAutocompleteElementResponse()
        if include_optional:
            return SupplyAutocompleteElementResponse(
                pki_supply_id = 85,
                s_supply_description_x = 'Letter paper package',
                b_supply_isactive = True
            )
        else:
            return SupplyAutocompleteElementResponse(
                pki_supply_id = 85,
                s_supply_description_x = 'Letter paper package',
                b_supply_isactive = True,
        )
        """

    def testSupplyAutocompleteElementResponse(self):
        """Test SupplyAutocompleteElementResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
