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

from eZmaxApi.models.custom_word_position_word_response import CustomWordPositionWordResponse

class TestCustomWordPositionWordResponse(unittest.TestCase):
    """CustomWordPositionWordResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CustomWordPositionWordResponse:
        """Test CustomWordPositionWordResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CustomWordPositionWordResponse`
        """
        model = CustomWordPositionWordResponse()
        if include_optional:
            return CustomWordPositionWordResponse(
                s_word = '',
                a_obj_word_position_occurence = [
                    eZmaxApi.models.custom_word_position_occurence_response.Custom-WordPositionOccurence-Response(
                        i_page = 1, 
                        i_x = 0, 
                        i_y = 0, )
                    ]
            )
        else:
            return CustomWordPositionWordResponse(
                s_word = '',
                a_obj_word_position_occurence = [
                    eZmaxApi.models.custom_word_position_occurence_response.Custom-WordPositionOccurence-Response(
                        i_page = 1, 
                        i_x = 0, 
                        i_y = 0, )
                    ],
        )
        """

    def testCustomWordPositionWordResponse(self):
        """Test CustomWordPositionWordResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
