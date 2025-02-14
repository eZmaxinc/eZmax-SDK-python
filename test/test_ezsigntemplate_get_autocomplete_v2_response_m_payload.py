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

from eZmaxApi.models.ezsigntemplate_get_autocomplete_v2_response_m_payload import EzsigntemplateGetAutocompleteV2ResponseMPayload

class TestEzsigntemplateGetAutocompleteV2ResponseMPayload(unittest.TestCase):
    """EzsigntemplateGetAutocompleteV2ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsigntemplateGetAutocompleteV2ResponseMPayload:
        """Test EzsigntemplateGetAutocompleteV2ResponseMPayload
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsigntemplateGetAutocompleteV2ResponseMPayload`
        """
        model = EzsigntemplateGetAutocompleteV2ResponseMPayload()
        if include_optional:
            return EzsigntemplateGetAutocompleteV2ResponseMPayload(
                a_obj_ezsigntemplate = [
                    eZmaxApi.models.ezsigntemplate_autocomplete_element_response.ezsigntemplate-AutocompleteElement-Response(
                        e_ezsignfoldertype_privacylevel = 'User', 
                        s_ezsigntemplate_description = 'Standard Contract', 
                        pki_ezsigntemplate_id = 36, 
                        b_ezsigntemplate_isactive = True, )
                    ]
            )
        else:
            return EzsigntemplateGetAutocompleteV2ResponseMPayload(
                a_obj_ezsigntemplate = [
                    eZmaxApi.models.ezsigntemplate_autocomplete_element_response.ezsigntemplate-AutocompleteElement-Response(
                        e_ezsignfoldertype_privacylevel = 'User', 
                        s_ezsigntemplate_description = 'Standard Contract', 
                        pki_ezsigntemplate_id = 36, 
                        b_ezsigntemplate_isactive = True, )
                    ],
        )
        """

    def testEzsigntemplateGetAutocompleteV2ResponseMPayload(self):
        """Test EzsigntemplateGetAutocompleteV2ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
