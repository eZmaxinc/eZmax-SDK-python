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

from eZmaxApi.models.ezsigndocument_get_ezsignsignatures_automatic_v1_response_m_payload import EzsigndocumentGetEzsignsignaturesAutomaticV1ResponseMPayload

class TestEzsigndocumentGetEzsignsignaturesAutomaticV1ResponseMPayload(unittest.TestCase):
    """EzsigndocumentGetEzsignsignaturesAutomaticV1ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsigndocumentGetEzsignsignaturesAutomaticV1ResponseMPayload:
        """Test EzsigndocumentGetEzsignsignaturesAutomaticV1ResponseMPayload
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsigndocumentGetEzsignsignaturesAutomaticV1ResponseMPayload`
        """
        model = EzsigndocumentGetEzsignsignaturesAutomaticV1ResponseMPayload()
        if include_optional:
            return EzsigndocumentGetEzsignsignaturesAutomaticV1ResponseMPayload(
                a_e_ezsignsignature_type = [
                    'Name'
                    ],
                a_obj_ezsignfolder = [
                    eZmaxApi.models.custom_ezsignfolder_ezsignsignatures_automatic_response.Custom-EzsignfolderEzsignsignaturesAutomatic-Response(
                        pki_ezsignfolder_id = 33, 
                        s_ezsignfolder_description = 'Test eZsign Folder', 
                        a_obj_ezsigndocument = [
                            eZmaxApi.models.custom_ezsigndocument_ezsignsignatures_automatic_response.Custom-EzsigndocumentEzsignsignaturesAutomatic-Response(
                                pki_ezsigndocument_id = 97, 
                                s_ezsigndocument_name = 'Contract #123', 
                                a_obj_ezsignsignature = [
                                    eZmaxApi.models.custom_ezsignsignature_ezsignsignatures_automatic_response.Custom-EzsignsignatureEzsignsignaturesAutomatic-Response(
                                        pki_ezsignsignature_id = 49, 
                                        e_ezsignsignature_type = 'Name', 
                                        i_ezsignpage_pagenumber = 1, )
                                    ], )
                            ], )
                    ]
            )
        else:
            return EzsigndocumentGetEzsignsignaturesAutomaticV1ResponseMPayload(
                a_e_ezsignsignature_type = [
                    'Name'
                    ],
                a_obj_ezsignfolder = [
                    eZmaxApi.models.custom_ezsignfolder_ezsignsignatures_automatic_response.Custom-EzsignfolderEzsignsignaturesAutomatic-Response(
                        pki_ezsignfolder_id = 33, 
                        s_ezsignfolder_description = 'Test eZsign Folder', 
                        a_obj_ezsigndocument = [
                            eZmaxApi.models.custom_ezsigndocument_ezsignsignatures_automatic_response.Custom-EzsigndocumentEzsignsignaturesAutomatic-Response(
                                pki_ezsigndocument_id = 97, 
                                s_ezsigndocument_name = 'Contract #123', 
                                a_obj_ezsignsignature = [
                                    eZmaxApi.models.custom_ezsignsignature_ezsignsignatures_automatic_response.Custom-EzsignsignatureEzsignsignaturesAutomatic-Response(
                                        pki_ezsignsignature_id = 49, 
                                        e_ezsignsignature_type = 'Name', 
                                        i_ezsignpage_pagenumber = 1, )
                                    ], )
                            ], )
                    ],
        )
        """

    def testEzsigndocumentGetEzsignsignaturesAutomaticV1ResponseMPayload(self):
        """Test EzsigndocumentGetEzsignsignaturesAutomaticV1ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
