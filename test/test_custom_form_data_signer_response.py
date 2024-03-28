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

from eZmaxApi.models.custom_form_data_signer_response import CustomFormDataSignerResponse

class TestCustomFormDataSignerResponse(unittest.TestCase):
    """CustomFormDataSignerResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CustomFormDataSignerResponse:
        """Test CustomFormDataSignerResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CustomFormDataSignerResponse`
        """
        model = CustomFormDataSignerResponse()
        if include_optional:
            return CustomFormDataSignerResponse(
                fki_ezsignfoldersignerassociation_id = 20,
                fki_user_id = 70,
                s_contact_firstname = 'John',
                s_contact_lastname = 'Doe',
                a_obj_ezsignformfieldgroup = [
                    eZmaxApi.models.custom_form_data_ezsignformfieldgroup_response.Custom-FormDataEzsignformfieldgroup-Response(
                        s_ezsignformfieldgroup_label = 'Allergies', 
                        a_obj_ezsignformfield = [
                            eZmaxApi.models.custom_form_data_ezsignformfield_response.Custom-FormDataEzsignformfield-Response(
                                s_ezsignformfield_label = 'Peanuts', 
                                s_ezsignformfield_value = 'Yes', )
                            ], )
                    ]
            )
        else:
            return CustomFormDataSignerResponse(
                fki_ezsignfoldersignerassociation_id = 20,
                s_contact_firstname = 'John',
                s_contact_lastname = 'Doe',
                a_obj_ezsignformfieldgroup = [
                    eZmaxApi.models.custom_form_data_ezsignformfieldgroup_response.Custom-FormDataEzsignformfieldgroup-Response(
                        s_ezsignformfieldgroup_label = 'Allergies', 
                        a_obj_ezsignformfield = [
                            eZmaxApi.models.custom_form_data_ezsignformfield_response.Custom-FormDataEzsignformfield-Response(
                                s_ezsignformfield_label = 'Peanuts', 
                                s_ezsignformfield_value = 'Yes', )
                            ], )
                    ],
        )
        """

    def testCustomFormDataSignerResponse(self):
        """Test CustomFormDataSignerResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
