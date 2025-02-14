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

from eZmaxApi.models.ezsignfoldertype_get_list_v1_response_m_payload import EzsignfoldertypeGetListV1ResponseMPayload

class TestEzsignfoldertypeGetListV1ResponseMPayload(unittest.TestCase):
    """EzsignfoldertypeGetListV1ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsignfoldertypeGetListV1ResponseMPayload:
        """Test EzsignfoldertypeGetListV1ResponseMPayload
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsignfoldertypeGetListV1ResponseMPayload`
        """
        model = EzsignfoldertypeGetListV1ResponseMPayload()
        if include_optional:
            return EzsignfoldertypeGetListV1ResponseMPayload(
                i_row_returned = 100,
                i_row_filtered = 533,
                a_obj_ezsignfoldertype = [
                    eZmaxApi.models.ezsignfoldertype_list_element.ezsignfoldertype-ListElement(
                        pki_ezsignfoldertype_id = 5, 
                        e_ezsignfoldertype_privacylevel = 'User', 
                        s_ezsignfoldertype_name_x = 'Default', 
                        b_ezsignfoldertype_isactive = True, )
                    ]
            )
        else:
            return EzsignfoldertypeGetListV1ResponseMPayload(
                i_row_returned = 100,
                i_row_filtered = 533,
                a_obj_ezsignfoldertype = [
                    eZmaxApi.models.ezsignfoldertype_list_element.ezsignfoldertype-ListElement(
                        pki_ezsignfoldertype_id = 5, 
                        e_ezsignfoldertype_privacylevel = 'User', 
                        s_ezsignfoldertype_name_x = 'Default', 
                        b_ezsignfoldertype_isactive = True, )
                    ],
        )
        """

    def testEzsignfoldertypeGetListV1ResponseMPayload(self):
        """Test EzsignfoldertypeGetListV1ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
