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

from eZmaxApi.models.ezsigntemplateglobal_get_autocomplete_v2_response_m_payload import EzsigntemplateglobalGetAutocompleteV2ResponseMPayload

class TestEzsigntemplateglobalGetAutocompleteV2ResponseMPayload(unittest.TestCase):
    """EzsigntemplateglobalGetAutocompleteV2ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsigntemplateglobalGetAutocompleteV2ResponseMPayload:
        """Test EzsigntemplateglobalGetAutocompleteV2ResponseMPayload
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsigntemplateglobalGetAutocompleteV2ResponseMPayload`
        """
        model = EzsigntemplateglobalGetAutocompleteV2ResponseMPayload()
        if include_optional:
            return EzsigntemplateglobalGetAutocompleteV2ResponseMPayload(
                a_obj_ezsigntemplateglobal = [
                    eZmaxApi.models.ezsigntemplateglobal_autocomplete_element_response.ezsigntemplateglobal-AutocompleteElement-Response(
                        pki_ezsigntemplateglobal_id = 36, 
                        s_ezsigntemplateglobal_description = 'Standard Contract', 
                        b_ezsigntemplateglobal_isactive = True, )
                    ]
            )
        else:
            return EzsigntemplateglobalGetAutocompleteV2ResponseMPayload(
                a_obj_ezsigntemplateglobal = [
                    eZmaxApi.models.ezsigntemplateglobal_autocomplete_element_response.ezsigntemplateglobal-AutocompleteElement-Response(
                        pki_ezsigntemplateglobal_id = 36, 
                        s_ezsigntemplateglobal_description = 'Standard Contract', 
                        b_ezsigntemplateglobal_isactive = True, )
                    ],
        )
        """

    def testEzsigntemplateglobalGetAutocompleteV2ResponseMPayload(self):
        """Test EzsigntemplateglobalGetAutocompleteV2ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
