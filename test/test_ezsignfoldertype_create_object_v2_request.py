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

from eZmaxApi.models.ezsignfoldertype_create_object_v2_request import EzsignfoldertypeCreateObjectV2Request

class TestEzsignfoldertypeCreateObjectV2Request(unittest.TestCase):
    """EzsignfoldertypeCreateObjectV2Request unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsignfoldertypeCreateObjectV2Request:
        """Test EzsignfoldertypeCreateObjectV2Request
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsignfoldertypeCreateObjectV2Request`
        """
        model = EzsignfoldertypeCreateObjectV2Request()
        if include_optional:
            return EzsignfoldertypeCreateObjectV2Request(
                a_obj_ezsignfoldertype = [
                    eZmaxApi.models.ezsignfoldertype_request_compound_v2.ezsignfoldertype-RequestCompoundV2()
                    ]
            )
        else:
            return EzsignfoldertypeCreateObjectV2Request(
                a_obj_ezsignfoldertype = [
                    eZmaxApi.models.ezsignfoldertype_request_compound_v2.ezsignfoldertype-RequestCompoundV2()
                    ],
        )
        """

    def testEzsignfoldertypeCreateObjectV2Request(self):
        """Test EzsignfoldertypeCreateObjectV2Request"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()