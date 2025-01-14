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

from eZmaxApi.models.sessionhistory_list_element import SessionhistoryListElement

class TestSessionhistoryListElement(unittest.TestCase):
    """SessionhistoryListElement unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SessionhistoryListElement:
        """Test SessionhistoryListElement
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SessionhistoryListElement`
        """
        model = SessionhistoryListElement()
        if include_optional:
            return SessionhistoryListElement(
                pki_sessionhistory_id = 259,
                fki_computer_id = 249,
                fki_user_id = 70,
                dt_sessionhistory_firsthit = '2020-12-31 17:35:37',
                dt_sessionhistory_lasthit = '2020-12-31 19:27:38',
                e_sessionhistory_endby = 'Logoff',
                s_computer_description = 'PC001',
                s_sessionhistory_duration = '01:52:01',
                s_sessionhistory_ip = '127.0.0.1',
                s_user_loginname = 'JohnDoe'
            )
        else:
            return SessionhistoryListElement(
                pki_sessionhistory_id = 259,
                dt_sessionhistory_firsthit = '2020-12-31 17:35:37',
                dt_sessionhistory_lasthit = '2020-12-31 19:27:38',
                e_sessionhistory_endby = 'Logoff',
                s_sessionhistory_duration = '01:52:01',
                s_sessionhistory_ip = '127.0.0.1',
        )
        """

    def testSessionhistoryListElement(self):
        """Test SessionhistoryListElement"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
