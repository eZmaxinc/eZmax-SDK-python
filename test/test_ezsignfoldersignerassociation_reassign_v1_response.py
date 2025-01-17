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

from eZmaxApi.models.ezsignfoldersignerassociation_reassign_v1_response import EzsignfoldersignerassociationReassignV1Response

class TestEzsignfoldersignerassociationReassignV1Response(unittest.TestCase):
    """EzsignfoldersignerassociationReassignV1Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsignfoldersignerassociationReassignV1Response:
        """Test EzsignfoldersignerassociationReassignV1Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsignfoldersignerassociationReassignV1Response`
        """
        model = EzsignfoldersignerassociationReassignV1Response()
        if include_optional:
            return EzsignfoldersignerassociationReassignV1Response(
            )
        else:
            return EzsignfoldersignerassociationReassignV1Response(
        )
        """

    def testEzsignfoldersignerassociationReassignV1Response(self):
        """Test EzsignfoldersignerassociationReassignV1Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
