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

from eZmaxApi.models.sessionhistory_get_list_v1_response_m_payload import SessionhistoryGetListV1ResponseMPayload

class TestSessionhistoryGetListV1ResponseMPayload(unittest.TestCase):
    """SessionhistoryGetListV1ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SessionhistoryGetListV1ResponseMPayload:
        """Test SessionhistoryGetListV1ResponseMPayload
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SessionhistoryGetListV1ResponseMPayload`
        """
        model = SessionhistoryGetListV1ResponseMPayload()
        if include_optional:
            return SessionhistoryGetListV1ResponseMPayload(
                i_row_returned = 100,
                i_row_filtered = 533,
                a_obj_sessionhistory = [
                    eZmaxApi.models.sessionhistory_list_element.sessionhistory-ListElement(
                        pki_sessionhistory_id = 259, 
                        fki_computer_id = 249, 
                        fki_user_id = 70, 
                        dt_sessionhistory_firsthit = '2020-12-31 17:35:37', 
                        dt_sessionhistory_lasthit = '2020-12-31 19:27:38', 
                        e_sessionhistory_endby = 'Logoff', 
                        s_computer_description = 'PC001', 
                        s_sessionhistory_duration = '01:52:01', 
                        s_sessionhistory_ip = '127.0.0.1', 
                        s_user_loginname = 'JohnDoe', )
                    ]
            )
        else:
            return SessionhistoryGetListV1ResponseMPayload(
                i_row_returned = 100,
                i_row_filtered = 533,
                a_obj_sessionhistory = [
                    eZmaxApi.models.sessionhistory_list_element.sessionhistory-ListElement(
                        pki_sessionhistory_id = 259, 
                        fki_computer_id = 249, 
                        fki_user_id = 70, 
                        dt_sessionhistory_firsthit = '2020-12-31 17:35:37', 
                        dt_sessionhistory_lasthit = '2020-12-31 19:27:38', 
                        e_sessionhistory_endby = 'Logoff', 
                        s_computer_description = 'PC001', 
                        s_sessionhistory_duration = '01:52:01', 
                        s_sessionhistory_ip = '127.0.0.1', 
                        s_user_loginname = 'JohnDoe', )
                    ],
        )
        """

    def testSessionhistoryGetListV1ResponseMPayload(self):
        """Test SessionhistoryGetListV1ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
