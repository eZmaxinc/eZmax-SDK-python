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

from eZmaxApi.models.ezsignfolder_get_list_v1_response_m_payload import EzsignfolderGetListV1ResponseMPayload

class TestEzsignfolderGetListV1ResponseMPayload(unittest.TestCase):
    """EzsignfolderGetListV1ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsignfolderGetListV1ResponseMPayload:
        """Test EzsignfolderGetListV1ResponseMPayload
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsignfolderGetListV1ResponseMPayload`
        """
        model = EzsignfolderGetListV1ResponseMPayload()
        if include_optional:
            return EzsignfolderGetListV1ResponseMPayload(
                i_row_returned = 100,
                i_row_filtered = 533,
                a_obj_ezsignfolder = [
                    eZmaxApi.models.ezsignfolder_list_element.ezsignfolder-ListElement(
                        pki_ezsignfolder_id = 33, 
                        fki_ezsignfoldertype_id = 5, 
                        e_ezsignfoldertype_privacylevel = 'User', 
                        s_ezsignfoldertype_name_x = 'Default', 
                        s_ezsignfolder_description = 'Test eZsign Folder', 
                        e_ezsignfolder_step = 'Completed', 
                        dt_created_date = '2020-12-31 23:59:59', 
                        dt_ezsignfolder_delayedsenddate = '2020-12-31T23:59:59.000Z', 
                        dt_ezsignfolder_sentdate = '2020-12-31T23:59:59.000Z', 
                        dt_ezsignfolder_duedate = '2020-12-31 23:59:59', 
                        i_ezsigndocument = 56, 
                        i_ezsigndocument_edm = 56, 
                        i_ezsignsignature = 56, 
                        i_ezsignsignature_signed = 56, 
                        i_ezsignformfieldgroup = 56, 
                        i_ezsignformfieldgroup_completed = 56, 
                        b_ezsignform_hasdependencies = True, 
                        d_ezsignfolder_completedpercentage = '-072.88', )
                    ]
            )
        else:
            return EzsignfolderGetListV1ResponseMPayload(
                i_row_returned = 100,
                i_row_filtered = 533,
                a_obj_ezsignfolder = [
                    eZmaxApi.models.ezsignfolder_list_element.ezsignfolder-ListElement(
                        pki_ezsignfolder_id = 33, 
                        fki_ezsignfoldertype_id = 5, 
                        e_ezsignfoldertype_privacylevel = 'User', 
                        s_ezsignfoldertype_name_x = 'Default', 
                        s_ezsignfolder_description = 'Test eZsign Folder', 
                        e_ezsignfolder_step = 'Completed', 
                        dt_created_date = '2020-12-31 23:59:59', 
                        dt_ezsignfolder_delayedsenddate = '2020-12-31T23:59:59.000Z', 
                        dt_ezsignfolder_sentdate = '2020-12-31T23:59:59.000Z', 
                        dt_ezsignfolder_duedate = '2020-12-31 23:59:59', 
                        i_ezsigndocument = 56, 
                        i_ezsigndocument_edm = 56, 
                        i_ezsignsignature = 56, 
                        i_ezsignsignature_signed = 56, 
                        i_ezsignformfieldgroup = 56, 
                        i_ezsignformfieldgroup_completed = 56, 
                        b_ezsignform_hasdependencies = True, 
                        d_ezsignfolder_completedpercentage = '-072.88', )
                    ],
        )
        """

    def testEzsignfolderGetListV1ResponseMPayload(self):
        """Test EzsignfolderGetListV1ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
