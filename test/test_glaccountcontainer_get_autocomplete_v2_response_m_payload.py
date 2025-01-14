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

from eZmaxApi.models.glaccountcontainer_get_autocomplete_v2_response_m_payload import GlaccountcontainerGetAutocompleteV2ResponseMPayload

class TestGlaccountcontainerGetAutocompleteV2ResponseMPayload(unittest.TestCase):
    """GlaccountcontainerGetAutocompleteV2ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GlaccountcontainerGetAutocompleteV2ResponseMPayload:
        """Test GlaccountcontainerGetAutocompleteV2ResponseMPayload
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GlaccountcontainerGetAutocompleteV2ResponseMPayload`
        """
        model = GlaccountcontainerGetAutocompleteV2ResponseMPayload()
        if include_optional:
            return GlaccountcontainerGetAutocompleteV2ResponseMPayload(
                a_obj_glaccountcontainer = [
                    eZmaxApi.models.glaccountcontainer_autocomplete_element_response.glaccountcontainer-AutocompleteElement-Response(
                        pki_glaccountcontainer_id = 66, 
                        s_glaccountcontainer_longcode = '5170.BARE1', 
                        s_glaccountcontainer_longdescription_x = 'Quebec', 
                        b_glaccountcontainer_isactive = True, )
                    ]
            )
        else:
            return GlaccountcontainerGetAutocompleteV2ResponseMPayload(
                a_obj_glaccountcontainer = [
                    eZmaxApi.models.glaccountcontainer_autocomplete_element_response.glaccountcontainer-AutocompleteElement-Response(
                        pki_glaccountcontainer_id = 66, 
                        s_glaccountcontainer_longcode = '5170.BARE1', 
                        s_glaccountcontainer_longdescription_x = 'Quebec', 
                        b_glaccountcontainer_isactive = True, )
                    ],
        )
        """

    def testGlaccountcontainerGetAutocompleteV2ResponseMPayload(self):
        """Test GlaccountcontainerGetAutocompleteV2ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
