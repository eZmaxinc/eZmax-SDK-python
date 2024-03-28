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

from eZmaxApi.models.activesession_get_list_v1_response_m_payload import ActivesessionGetListV1ResponseMPayload

class TestActivesessionGetListV1ResponseMPayload(unittest.TestCase):
    """ActivesessionGetListV1ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ActivesessionGetListV1ResponseMPayload:
        """Test ActivesessionGetListV1ResponseMPayload
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ActivesessionGetListV1ResponseMPayload`
        """
        model = ActivesessionGetListV1ResponseMPayload()
        if include_optional:
            return ActivesessionGetListV1ResponseMPayload(
                i_row_returned = 100,
                i_row_filtered = 533,
                a_obj_activesession = [
                    eZmaxApi.models.activesession_list_element.activesession-ListElement(
                        pki_activesession_id = 16, 
                        fki_user_id = 70, 
                        fki_computer_id = 249, 
                        fki_company_id = 1, 
                        fki_department_id = 21, 
                        s_company_name_x = 'Acme inc.', 
                        s_department_name_x = 'Head Office', 
                        s_activesession_loginname = 'doej', 
                        s_computer_description = 'PC001', 
                        dt_activesession_firsthit = '2020-12-31 23:59:59', 
                        dt_activesession_lasthit = '2020-12-31 23:59:59', 
                        s_activesession_ip = '127.0.0.1', )
                    ]
            )
        else:
            return ActivesessionGetListV1ResponseMPayload(
                i_row_returned = 100,
                i_row_filtered = 533,
                a_obj_activesession = [
                    eZmaxApi.models.activesession_list_element.activesession-ListElement(
                        pki_activesession_id = 16, 
                        fki_user_id = 70, 
                        fki_computer_id = 249, 
                        fki_company_id = 1, 
                        fki_department_id = 21, 
                        s_company_name_x = 'Acme inc.', 
                        s_department_name_x = 'Head Office', 
                        s_activesession_loginname = 'doej', 
                        s_computer_description = 'PC001', 
                        dt_activesession_firsthit = '2020-12-31 23:59:59', 
                        dt_activesession_lasthit = '2020-12-31 23:59:59', 
                        s_activesession_ip = '127.0.0.1', )
                    ],
        )
        """

    def testActivesessionGetListV1ResponseMPayload(self):
        """Test ActivesessionGetListV1ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
