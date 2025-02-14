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

from eZmaxApi.models.ezsignsignergroup_create_object_v1_request import EzsignsignergroupCreateObjectV1Request

class TestEzsignsignergroupCreateObjectV1Request(unittest.TestCase):
    """EzsignsignergroupCreateObjectV1Request unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsignsignergroupCreateObjectV1Request:
        """Test EzsignsignergroupCreateObjectV1Request
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsignsignergroupCreateObjectV1Request`
        """
        model = EzsignsignergroupCreateObjectV1Request()
        if include_optional:
            return EzsignsignergroupCreateObjectV1Request(
                a_obj_ezsignsignergroup = [
                    eZmaxApi.models.ezsignsignergroup_request_compound.ezsignsignergroup-RequestCompound()
                    ]
            )
        else:
            return EzsignsignergroupCreateObjectV1Request(
                a_obj_ezsignsignergroup = [
                    eZmaxApi.models.ezsignsignergroup_request_compound.ezsignsignergroup-RequestCompound()
                    ],
        )
        """

    def testEzsignsignergroupCreateObjectV1Request(self):
        """Test EzsignsignergroupCreateObjectV1Request"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
