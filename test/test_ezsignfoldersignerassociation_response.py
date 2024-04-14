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

from eZmaxApi.models.ezsignfoldersignerassociation_response import EzsignfoldersignerassociationResponse

class TestEzsignfoldersignerassociationResponse(unittest.TestCase):
    """EzsignfoldersignerassociationResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsignfoldersignerassociationResponse:
        """Test EzsignfoldersignerassociationResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsignfoldersignerassociationResponse`
        """
        model = EzsignfoldersignerassociationResponse()
        if include_optional:
            return EzsignfoldersignerassociationResponse(
                pki_ezsignfoldersignerassociation_id = 20,
                fki_ezsignfolder_id = 33,
                b_ezsignfoldersignerassociation_delayedsend = True,
                b_ezsignfoldersignerassociation_receivecopy = True,
                t_ezsignfoldersignerassociation_message = 'Hi John,

This is the document I need you to review.

Could you sign it before Monday please.

Best Regards.

Mary',
                b_ezsignfoldersignerassociation_allowsigninginperson = True
            )
        else:
            return EzsignfoldersignerassociationResponse(
                pki_ezsignfoldersignerassociation_id = 20,
                fki_ezsignfolder_id = 33,
                b_ezsignfoldersignerassociation_delayedsend = True,
                b_ezsignfoldersignerassociation_receivecopy = True,
                t_ezsignfoldersignerassociation_message = 'Hi John,

This is the document I need you to review.

Could you sign it before Monday please.

Best Regards.

Mary',
                b_ezsignfoldersignerassociation_allowsigninginperson = True,
        )
        """

    def testEzsignfoldersignerassociationResponse(self):
        """Test EzsignfoldersignerassociationResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
