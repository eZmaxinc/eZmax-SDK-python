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

from eZmaxApi.models.custom_ezsignformfield_request import CustomEzsignformfieldRequest

class TestCustomEzsignformfieldRequest(unittest.TestCase):
    """CustomEzsignformfieldRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CustomEzsignformfieldRequest:
        """Test CustomEzsignformfieldRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CustomEzsignformfieldRequest`
        """
        model = CustomEzsignformfieldRequest()
        if include_optional:
            return CustomEzsignformfieldRequest(
                pki_ezsignformfield_id = 32,
                s_ezsignformfield_label = 'Peanuts',
                b_ezsignformfield_selected = True,
                s_ezsignformfield_enteredvalue = 'Montreal'
            )
        else:
            return CustomEzsignformfieldRequest(
        )
        """

    def testCustomEzsignformfieldRequest(self):
        """Test CustomEzsignformfieldRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
