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

from eZmaxApi.models.custom_ezsignfoldersignerassociation_actionable_element_response import CustomEzsignfoldersignerassociationActionableElementResponse  # noqa: E501

class TestCustomEzsignfoldersignerassociationActionableElementResponse(unittest.TestCase):
    """CustomEzsignfoldersignerassociationActionableElementResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CustomEzsignfoldersignerassociationActionableElementResponse:
        """Test CustomEzsignfoldersignerassociationActionableElementResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CustomEzsignfoldersignerassociationActionableElementResponse`
        """
        model = CustomEzsignfoldersignerassociationActionableElementResponse()  # noqa: E501
        if include_optional:
            return CustomEzsignfoldersignerassociationActionableElementResponse(
                pki_ezsignfoldersignerassociation_id = 20,
                fki_ezsignfolder_id = 33,
                b_ezsignfoldersignerassociation_delayedsend = True,
                b_ezsignfoldersignerassociation_receivecopy = True,
                t_ezsignfoldersignerassociation_message = 'Hi John,

This is the document I need you to review.

Could you sign it before Monday please.

Best Regards.

Mary',
                obj_ezsignsignergroup = eZmaxApi.models.ezsignsignergroup_response_compound.ezsignsignergroup-ResponseCompound(),
                obj_user = eZmaxApi.models.ezsignfoldersignerassociation_response_compound_user.ezsignfoldersignerassociation-ResponseCompound-User(
                    pki_user_id = 70, 
                    fki_language_id = 2, 
                    s_user_firstname = 'John', 
                    s_user_lastname = 'Doe', 
                    s_email_address = 'email@example.com', ),
                obj_ezsignsigner = eZmaxApi.models.ezsignsigner_response_compound.ezsignsigner-ResponseCompound(),
                b_ezsignfoldersignerassociation_hasactionableelements_current = True,
                b_ezsignfoldersignerassociation_hasactionableelements_future = True
            )
        else:
            return CustomEzsignfoldersignerassociationActionableElementResponse(
                pki_ezsignfoldersignerassociation_id = 20,
                fki_ezsignfolder_id = 33,
                b_ezsignfoldersignerassociation_delayedsend = True,
                b_ezsignfoldersignerassociation_receivecopy = True,
                t_ezsignfoldersignerassociation_message = 'Hi John,

This is the document I need you to review.

Could you sign it before Monday please.

Best Regards.

Mary',
                b_ezsignfoldersignerassociation_hasactionableelements_current = True,
        )
        """

    def testCustomEzsignfoldersignerassociationActionableElementResponse(self):
        """Test CustomEzsignfoldersignerassociationActionableElementResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
