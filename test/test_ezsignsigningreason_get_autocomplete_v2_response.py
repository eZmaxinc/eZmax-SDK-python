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

from eZmaxApi.models.ezsignsigningreason_get_autocomplete_v2_response import EzsignsigningreasonGetAutocompleteV2Response

class TestEzsignsigningreasonGetAutocompleteV2Response(unittest.TestCase):
    """EzsignsigningreasonGetAutocompleteV2Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsignsigningreasonGetAutocompleteV2Response:
        """Test EzsignsigningreasonGetAutocompleteV2Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsignsigningreasonGetAutocompleteV2Response`
        """
        model = EzsignsigningreasonGetAutocompleteV2Response()
        if include_optional:
            return EzsignsigningreasonGetAutocompleteV2Response(
                m_payload = eZmaxApi.models.ezsignsigningreason_get_autocomplete_v2_response_m_payload.ezsignsigningreason-getAutocomplete-v2-Response-mPayload(
                    a_obj_ezsignsigningreason = [
                        eZmaxApi.models.ezsignsigningreason_autocomplete_element_response.ezsignsigningreason-AutocompleteElement-Response(
                            pki_ezsignsigningreason_id = 194, 
                            s_ezsignsigningreason_description_x = 'I approve this document', 
                            b_ezsignsigningreason_isactive = True, )
                        ], )
            )
        else:
            return EzsignsigningreasonGetAutocompleteV2Response(
                m_payload = eZmaxApi.models.ezsignsigningreason_get_autocomplete_v2_response_m_payload.ezsignsigningreason-getAutocomplete-v2-Response-mPayload(
                    a_obj_ezsignsigningreason = [
                        eZmaxApi.models.ezsignsigningreason_autocomplete_element_response.ezsignsigningreason-AutocompleteElement-Response(
                            pki_ezsignsigningreason_id = 194, 
                            s_ezsignsigningreason_description_x = 'I approve this document', 
                            b_ezsignsigningreason_isactive = True, )
                        ], ),
        )
        """

    def testEzsignsigningreasonGetAutocompleteV2Response(self):
        """Test EzsignsigningreasonGetAutocompleteV2Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
