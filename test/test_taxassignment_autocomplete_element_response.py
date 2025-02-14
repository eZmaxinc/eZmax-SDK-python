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

from eZmaxApi.models.taxassignment_autocomplete_element_response import TaxassignmentAutocompleteElementResponse

class TestTaxassignmentAutocompleteElementResponse(unittest.TestCase):
    """TaxassignmentAutocompleteElementResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TaxassignmentAutocompleteElementResponse:
        """Test TaxassignmentAutocompleteElementResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TaxassignmentAutocompleteElementResponse`
        """
        model = TaxassignmentAutocompleteElementResponse()
        if include_optional:
            return TaxassignmentAutocompleteElementResponse(
                s_taxassignment_description_x = 'Default',
                pki_taxassignment_id = 1,
                b_taxassignment_isactive = True
            )
        else:
            return TaxassignmentAutocompleteElementResponse(
                s_taxassignment_description_x = 'Default',
                pki_taxassignment_id = 1,
                b_taxassignment_isactive = True,
        )
        """

    def testTaxassignmentAutocompleteElementResponse(self):
        """Test TaxassignmentAutocompleteElementResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
