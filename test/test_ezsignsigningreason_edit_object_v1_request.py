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

from eZmaxApi.models.ezsignsigningreason_edit_object_v1_request import EzsignsigningreasonEditObjectV1Request

class TestEzsignsigningreasonEditObjectV1Request(unittest.TestCase):
    """EzsignsigningreasonEditObjectV1Request unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsignsigningreasonEditObjectV1Request:
        """Test EzsignsigningreasonEditObjectV1Request
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsignsigningreasonEditObjectV1Request`
        """
        model = EzsignsigningreasonEditObjectV1Request()
        if include_optional:
            return EzsignsigningreasonEditObjectV1Request(
                obj_ezsignsigningreason = eZmaxApi.models.ezsignsigningreason_request_compound.ezsignsigningreason-RequestCompound()
            )
        else:
            return EzsignsigningreasonEditObjectV1Request(
                obj_ezsignsigningreason = eZmaxApi.models.ezsignsigningreason_request_compound.ezsignsigningreason-RequestCompound(),
        )
        """

    def testEzsignsigningreasonEditObjectV1Request(self):
        """Test EzsignsigningreasonEditObjectV1Request"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
