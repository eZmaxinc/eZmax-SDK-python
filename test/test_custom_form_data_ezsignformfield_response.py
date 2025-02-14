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

from eZmaxApi.models.custom_form_data_ezsignformfield_response import CustomFormDataEzsignformfieldResponse

class TestCustomFormDataEzsignformfieldResponse(unittest.TestCase):
    """CustomFormDataEzsignformfieldResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CustomFormDataEzsignformfieldResponse:
        """Test CustomFormDataEzsignformfieldResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CustomFormDataEzsignformfieldResponse`
        """
        model = CustomFormDataEzsignformfieldResponse()
        if include_optional:
            return CustomFormDataEzsignformfieldResponse(
                s_ezsignformfield_label = 'Peanuts',
                s_ezsignformfield_value = 'Yes'
            )
        else:
            return CustomFormDataEzsignformfieldResponse(
                s_ezsignformfield_label = 'Peanuts',
                s_ezsignformfield_value = 'Yes',
        )
        """

    def testCustomFormDataEzsignformfieldResponse(self):
        """Test CustomFormDataEzsignformfieldResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
