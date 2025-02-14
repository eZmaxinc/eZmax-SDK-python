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

from eZmaxApi.models.ezsignfoldersignerassociation_reassign_v1_request import EzsignfoldersignerassociationReassignV1Request

class TestEzsignfoldersignerassociationReassignV1Request(unittest.TestCase):
    """EzsignfoldersignerassociationReassignV1Request unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsignfoldersignerassociationReassignV1Request:
        """Test EzsignfoldersignerassociationReassignV1Request
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsignfoldersignerassociationReassignV1Request`
        """
        model = EzsignfoldersignerassociationReassignV1Request()
        if include_optional:
            return EzsignfoldersignerassociationReassignV1Request(
                fki_ezsignfoldersignerassociation_id = 20
            )
        else:
            return EzsignfoldersignerassociationReassignV1Request(
        )
        """

    def testEzsignfoldersignerassociationReassignV1Request(self):
        """Test EzsignfoldersignerassociationReassignV1Request"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
