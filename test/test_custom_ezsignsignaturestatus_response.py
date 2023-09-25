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

from eZmaxApi.models.custom_ezsignsignaturestatus_response import CustomEzsignsignaturestatusResponse  # noqa: E501

class TestCustomEzsignsignaturestatusResponse(unittest.TestCase):
    """CustomEzsignsignaturestatusResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CustomEzsignsignaturestatusResponse:
        """Test CustomEzsignsignaturestatusResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CustomEzsignsignaturestatusResponse`
        """
        model = CustomEzsignsignaturestatusResponse()  # noqa: E501
        if include_optional:
            return CustomEzsignsignaturestatusResponse(
                e_ezsignsignaturestatus_steptype = 'Form',
                i_ezsignsignaturestatus_step = 1,
                i_ezsignsignaturestatus_total = 2,
                i_ezsignsignaturestatus_signed = 1
            )
        else:
            return CustomEzsignsignaturestatusResponse(
                e_ezsignsignaturestatus_steptype = 'Form',
                i_ezsignsignaturestatus_step = 1,
                i_ezsignsignaturestatus_total = 2,
                i_ezsignsignaturestatus_signed = 1,
        )
        """

    def testCustomEzsignsignaturestatusResponse(self):
        """Test CustomEzsignsignaturestatusResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
