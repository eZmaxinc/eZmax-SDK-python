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

from eZmaxApi.models.phonetype_get_autocomplete_v2_response_m_payload import PhonetypeGetAutocompleteV2ResponseMPayload  # noqa: E501

class TestPhonetypeGetAutocompleteV2ResponseMPayload(unittest.TestCase):
    """PhonetypeGetAutocompleteV2ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PhonetypeGetAutocompleteV2ResponseMPayload:
        """Test PhonetypeGetAutocompleteV2ResponseMPayload
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PhonetypeGetAutocompleteV2ResponseMPayload`
        """
        model = PhonetypeGetAutocompleteV2ResponseMPayload()  # noqa: E501
        if include_optional:
            return PhonetypeGetAutocompleteV2ResponseMPayload(
                a_obj_phonetype = [
                    eZmaxApi.models.phonetype_autocomplete_element_response.phonetype-AutocompleteElement-Response(
                        pki_phonetype_id = 1, 
                        s_phonetype_name_x = 'Office', 
                        b_phonetype_isactive = True, )
                    ]
            )
        else:
            return PhonetypeGetAutocompleteV2ResponseMPayload(
        )
        """

    def testPhonetypeGetAutocompleteV2ResponseMPayload(self):
        """Test PhonetypeGetAutocompleteV2ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
