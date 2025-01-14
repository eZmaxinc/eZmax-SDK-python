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

from eZmaxApi.models.ezsignfolder_import_ezsignfoldersignerassociations_v1_request import EzsignfolderImportEzsignfoldersignerassociationsV1Request

class TestEzsignfolderImportEzsignfoldersignerassociationsV1Request(unittest.TestCase):
    """EzsignfolderImportEzsignfoldersignerassociationsV1Request unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsignfolderImportEzsignfoldersignerassociationsV1Request:
        """Test EzsignfolderImportEzsignfoldersignerassociationsV1Request
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsignfolderImportEzsignfoldersignerassociationsV1Request`
        """
        model = EzsignfolderImportEzsignfoldersignerassociationsV1Request()
        if include_optional:
            return EzsignfolderImportEzsignfoldersignerassociationsV1Request(
                a_fki_ezsignfoldersignerassociation_id = [
                    20
                    ]
            )
        else:
            return EzsignfolderImportEzsignfoldersignerassociationsV1Request(
                a_fki_ezsignfoldersignerassociation_id = [
                    20
                    ],
        )
        """

    def testEzsignfolderImportEzsignfoldersignerassociationsV1Request(self):
        """Test EzsignfolderImportEzsignfoldersignerassociationsV1Request"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
