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

from eZmaxApi.models.franchiseoffice_get_autocomplete_v2_response_m_payload import FranchiseofficeGetAutocompleteV2ResponseMPayload

class TestFranchiseofficeGetAutocompleteV2ResponseMPayload(unittest.TestCase):
    """FranchiseofficeGetAutocompleteV2ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FranchiseofficeGetAutocompleteV2ResponseMPayload:
        """Test FranchiseofficeGetAutocompleteV2ResponseMPayload
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FranchiseofficeGetAutocompleteV2ResponseMPayload`
        """
        model = FranchiseofficeGetAutocompleteV2ResponseMPayload()
        if include_optional:
            return FranchiseofficeGetAutocompleteV2ResponseMPayload(
                a_obj_franchiseoffice = [
                    eZmaxApi.models.franchiseoffice_autocomplete_element_response.franchiseoffice-AutocompleteElement-Response(
                        s_franchiseoffice_description = 'Default', 
                        pki_franchiseoffice_id = 50, 
                        b_franchiseoffice_isactive = True, )
                    ]
            )
        else:
            return FranchiseofficeGetAutocompleteV2ResponseMPayload(
                a_obj_franchiseoffice = [
                    eZmaxApi.models.franchiseoffice_autocomplete_element_response.franchiseoffice-AutocompleteElement-Response(
                        s_franchiseoffice_description = 'Default', 
                        pki_franchiseoffice_id = 50, 
                        b_franchiseoffice_isactive = True, )
                    ],
        )
        """

    def testFranchiseofficeGetAutocompleteV2ResponseMPayload(self):
        """Test FranchiseofficeGetAutocompleteV2ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
