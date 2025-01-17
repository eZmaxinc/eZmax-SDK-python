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

from eZmaxApi.models.usergroup_get_list_v1_response_m_payload import UsergroupGetListV1ResponseMPayload

class TestUsergroupGetListV1ResponseMPayload(unittest.TestCase):
    """UsergroupGetListV1ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UsergroupGetListV1ResponseMPayload:
        """Test UsergroupGetListV1ResponseMPayload
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UsergroupGetListV1ResponseMPayload`
        """
        model = UsergroupGetListV1ResponseMPayload()
        if include_optional:
            return UsergroupGetListV1ResponseMPayload(
                a_obj_usergroup = [
                    eZmaxApi.models.usergroup_list_element.usergroup-ListElement(
                        pki_usergroup_id = 2, 
                        s_usergroup_name_x = 'Administration', 
                        i_count_user = 15, )
                    ]
            )
        else:
            return UsergroupGetListV1ResponseMPayload(
                a_obj_usergroup = [
                    eZmaxApi.models.usergroup_list_element.usergroup-ListElement(
                        pki_usergroup_id = 2, 
                        s_usergroup_name_x = 'Administration', 
                        i_count_user = 15, )
                    ],
        )
        """

    def testUsergroupGetListV1ResponseMPayload(self):
        """Test UsergroupGetListV1ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
