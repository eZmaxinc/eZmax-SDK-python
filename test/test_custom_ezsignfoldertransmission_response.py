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

from eZmaxApi.models.custom_ezsignfoldertransmission_response import CustomEzsignfoldertransmissionResponse  # noqa: E501

class TestCustomEzsignfoldertransmissionResponse(unittest.TestCase):
    """CustomEzsignfoldertransmissionResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CustomEzsignfoldertransmissionResponse:
        """Test CustomEzsignfoldertransmissionResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CustomEzsignfoldertransmissionResponse`
        """
        model = CustomEzsignfoldertransmissionResponse()  # noqa: E501
        if include_optional:
            return CustomEzsignfoldertransmissionResponse(
                pki_ezsignfolder_id = 33,
                s_ezsignfolder_description = 'Test eZsign Folder',
                e_ezsignfolder_step = 'Completed',
                i_ezsignfolder_signaturetotal = 4,
                i_ezsignfolder_signaturesigned = 3,
                a_obj_ezsignfoldertransmission_signer = [
                    eZmaxApi.models.custom_ezsignfoldertransmission_signer_response.Custom-EzsignfoldertransmissionSigner-Response(
                        fki_user_id = 70, 
                        s_contact_firstname = 'John', 
                        s_contact_lastname = 'Doe', )
                    ]
            )
        else:
            return CustomEzsignfoldertransmissionResponse(
                pki_ezsignfolder_id = 33,
                s_ezsignfolder_description = 'Test eZsign Folder',
                e_ezsignfolder_step = 'Completed',
                i_ezsignfolder_signaturetotal = 4,
                i_ezsignfolder_signaturesigned = 3,
                a_obj_ezsignfoldertransmission_signer = [
                    eZmaxApi.models.custom_ezsignfoldertransmission_signer_response.Custom-EzsignfoldertransmissionSigner-Response(
                        fki_user_id = 70, 
                        s_contact_firstname = 'John', 
                        s_contact_lastname = 'Doe', )
                    ],
        )
        """

    def testCustomEzsignfoldertransmissionResponse(self):
        """Test CustomEzsignfoldertransmissionResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
