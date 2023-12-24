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

from eZmaxApi.models.ezsignfoldersignerassociation_edit_object_v1_request import EzsignfoldersignerassociationEditObjectV1Request

class TestEzsignfoldersignerassociationEditObjectV1Request(unittest.TestCase):
    """EzsignfoldersignerassociationEditObjectV1Request unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsignfoldersignerassociationEditObjectV1Request:
        """Test EzsignfoldersignerassociationEditObjectV1Request
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsignfoldersignerassociationEditObjectV1Request`
        """
        model = EzsignfoldersignerassociationEditObjectV1Request()
        if include_optional:
            return EzsignfoldersignerassociationEditObjectV1Request(
                obj_ezsignfoldersignerassociation = eZmaxApi.models.ezsignfoldersignerassociation_request_compound.ezsignfoldersignerassociation-RequestCompound()
            )
        else:
            return EzsignfoldersignerassociationEditObjectV1Request(
                obj_ezsignfoldersignerassociation = eZmaxApi.models.ezsignfoldersignerassociation_request_compound.ezsignfoldersignerassociation-RequestCompound(),
        )
        """

    def testEzsignfoldersignerassociationEditObjectV1Request(self):
        """Test EzsignfoldersignerassociationEditObjectV1Request"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
