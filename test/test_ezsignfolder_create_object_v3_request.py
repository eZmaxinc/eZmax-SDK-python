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

from eZmaxApi.models.ezsignfolder_create_object_v3_request import EzsignfolderCreateObjectV3Request

class TestEzsignfolderCreateObjectV3Request(unittest.TestCase):
    """EzsignfolderCreateObjectV3Request unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsignfolderCreateObjectV3Request:
        """Test EzsignfolderCreateObjectV3Request
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsignfolderCreateObjectV3Request`
        """
        model = EzsignfolderCreateObjectV3Request()
        if include_optional:
            return EzsignfolderCreateObjectV3Request(
                a_obj_ezsignfolder = [
                    eZmaxApi.models.ezsignfolder_request_compound_v3.ezsignfolder-RequestCompoundV3()
                    ]
            )
        else:
            return EzsignfolderCreateObjectV3Request(
                a_obj_ezsignfolder = [
                    eZmaxApi.models.ezsignfolder_request_compound_v3.ezsignfolder-RequestCompoundV3()
                    ],
        )
        """

    def testEzsignfolderCreateObjectV3Request(self):
        """Test EzsignfolderCreateObjectV3Request"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
