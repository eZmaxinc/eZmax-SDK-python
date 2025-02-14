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

from eZmaxApi.models.ezsignfolder_get_ezsignfoldersignerassociations_v1_response_m_payload import EzsignfolderGetEzsignfoldersignerassociationsV1ResponseMPayload

class TestEzsignfolderGetEzsignfoldersignerassociationsV1ResponseMPayload(unittest.TestCase):
    """EzsignfolderGetEzsignfoldersignerassociationsV1ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsignfolderGetEzsignfoldersignerassociationsV1ResponseMPayload:
        """Test EzsignfolderGetEzsignfoldersignerassociationsV1ResponseMPayload
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsignfolderGetEzsignfoldersignerassociationsV1ResponseMPayload`
        """
        model = EzsignfolderGetEzsignfoldersignerassociationsV1ResponseMPayload()
        if include_optional:
            return EzsignfolderGetEzsignfoldersignerassociationsV1ResponseMPayload(
                a_obj_ezsignfoldersignerassociation = [
                    eZmaxApi.models.custom_ezsignfoldersignerassociation_actionable_element_response.Custom-EzsignfoldersignerassociationActionableElement-Response()
                    ]
            )
        else:
            return EzsignfolderGetEzsignfoldersignerassociationsV1ResponseMPayload(
                a_obj_ezsignfoldersignerassociation = [
                    eZmaxApi.models.custom_ezsignfoldersignerassociation_actionable_element_response.Custom-EzsignfoldersignerassociationActionableElement-Response()
                    ],
        )
        """

    def testEzsignfolderGetEzsignfoldersignerassociationsV1ResponseMPayload(self):
        """Test EzsignfolderGetEzsignfoldersignerassociationsV1ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
