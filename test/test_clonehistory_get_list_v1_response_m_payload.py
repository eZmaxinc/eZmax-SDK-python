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

from eZmaxApi.models.clonehistory_get_list_v1_response_m_payload import ClonehistoryGetListV1ResponseMPayload

class TestClonehistoryGetListV1ResponseMPayload(unittest.TestCase):
    """ClonehistoryGetListV1ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ClonehistoryGetListV1ResponseMPayload:
        """Test ClonehistoryGetListV1ResponseMPayload
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ClonehistoryGetListV1ResponseMPayload`
        """
        model = ClonehistoryGetListV1ResponseMPayload()
        if include_optional:
            return ClonehistoryGetListV1ResponseMPayload(
                i_row_returned = 100,
                i_row_filtered = 533,
                a_obj_clonehistory = [
                    eZmaxApi.models.clonehistory_list_element.clonehistory-ListElement(
                        pki_clonehistory_id = 12, 
                        fki_user_id_cloning = 70, 
                        fki_user_id_cloned = 70, 
                        dt_clonehistory_firsthit = '2020-12-31 23:59:59', 
                        dt_clonehistory_lasthit = '2020-12-31 23:59:59', 
                        s_user_loginname_cloning = 'JohnDoe', 
                        s_user_firstname_cloning = 'John', 
                        s_user_lastname_cloning = 'Doe', 
                        s_user_loginname_cloned = 'JohnDoe', 
                        s_user_firstname_cloned = 'John', 
                        s_user_lastname_cloned = 'Doe', )
                    ]
            )
        else:
            return ClonehistoryGetListV1ResponseMPayload(
                i_row_returned = 100,
                i_row_filtered = 533,
                a_obj_clonehistory = [
                    eZmaxApi.models.clonehistory_list_element.clonehistory-ListElement(
                        pki_clonehistory_id = 12, 
                        fki_user_id_cloning = 70, 
                        fki_user_id_cloned = 70, 
                        dt_clonehistory_firsthit = '2020-12-31 23:59:59', 
                        dt_clonehistory_lasthit = '2020-12-31 23:59:59', 
                        s_user_loginname_cloning = 'JohnDoe', 
                        s_user_firstname_cloning = 'John', 
                        s_user_lastname_cloning = 'Doe', 
                        s_user_loginname_cloned = 'JohnDoe', 
                        s_user_firstname_cloned = 'John', 
                        s_user_lastname_cloned = 'Doe', )
                    ],
        )
        """

    def testClonehistoryGetListV1ResponseMPayload(self):
        """Test ClonehistoryGetListV1ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
