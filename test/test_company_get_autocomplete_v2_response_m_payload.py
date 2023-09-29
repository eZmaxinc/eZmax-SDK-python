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

from eZmaxApi.models.company_get_autocomplete_v2_response_m_payload import CompanyGetAutocompleteV2ResponseMPayload  # noqa: E501

class TestCompanyGetAutocompleteV2ResponseMPayload(unittest.TestCase):
    """CompanyGetAutocompleteV2ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CompanyGetAutocompleteV2ResponseMPayload:
        """Test CompanyGetAutocompleteV2ResponseMPayload
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CompanyGetAutocompleteV2ResponseMPayload`
        """
        model = CompanyGetAutocompleteV2ResponseMPayload()  # noqa: E501
        if include_optional:
            return CompanyGetAutocompleteV2ResponseMPayload(
                a_obj_company = [
                    eZmaxApi.models.company_autocomplete_element_response.company-AutocompleteElement-Response(
                        pki_company_id = 1, 
                        s_company_name_x = 'Acme inc.', 
                        b_company_isactive = True, )
                    ]
            )
        else:
            return CompanyGetAutocompleteV2ResponseMPayload(
        )
        """

    def testCompanyGetAutocompleteV2ResponseMPayload(self):
        """Test CompanyGetAutocompleteV2ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()