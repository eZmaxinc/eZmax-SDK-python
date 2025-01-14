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

from eZmaxApi.models.custom_dropdown_element_response import CustomDropdownElementResponse

class TestCustomDropdownElementResponse(unittest.TestCase):
    """CustomDropdownElementResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CustomDropdownElementResponse:
        """Test CustomDropdownElementResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CustomDropdownElementResponse`
        """
        model = CustomDropdownElementResponse()
        if include_optional:
            return CustomDropdownElementResponse(
                s_label = '',
                s_value = ''
            )
        else:
            return CustomDropdownElementResponse(
                s_label = '',
                s_value = '',
        )
        """

    def testCustomDropdownElementResponse(self):
        """Test CustomDropdownElementResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
