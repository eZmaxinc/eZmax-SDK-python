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

from eZmaxApi.models.ezsignfolder_edit_object_v1_request import EzsignfolderEditObjectV1Request

class TestEzsignfolderEditObjectV1Request(unittest.TestCase):
    """EzsignfolderEditObjectV1Request unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsignfolderEditObjectV1Request:
        """Test EzsignfolderEditObjectV1Request
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsignfolderEditObjectV1Request`
        """
        model = EzsignfolderEditObjectV1Request()
        if include_optional:
            return EzsignfolderEditObjectV1Request(
                obj_ezsignfolder = eZmaxApi.models.ezsignfolder_request_compound.ezsignfolder-RequestCompound()
            )
        else:
            return EzsignfolderEditObjectV1Request(
                obj_ezsignfolder = eZmaxApi.models.ezsignfolder_request_compound.ezsignfolder-RequestCompound(),
        )
        """

    def testEzsignfolderEditObjectV1Request(self):
        """Test EzsignfolderEditObjectV1Request"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
