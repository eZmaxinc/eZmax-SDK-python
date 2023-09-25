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

from eZmaxApi.models.clonehistory_list_element import ClonehistoryListElement  # noqa: E501

class TestClonehistoryListElement(unittest.TestCase):
    """ClonehistoryListElement unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ClonehistoryListElement:
        """Test ClonehistoryListElement
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ClonehistoryListElement`
        """
        model = ClonehistoryListElement()  # noqa: E501
        if include_optional:
            return ClonehistoryListElement(
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
                s_user_lastname_cloned = 'Doe'
            )
        else:
            return ClonehistoryListElement(
                pki_clonehistory_id = 12,
                fki_user_id_cloning = 70,
                fki_user_id_cloned = 70,
                dt_clonehistory_firsthit = '2020-12-31 23:59:59',
                s_user_loginname_cloning = 'JohnDoe',
                s_user_firstname_cloning = 'John',
                s_user_lastname_cloning = 'Doe',
                s_user_loginname_cloned = 'JohnDoe',
                s_user_firstname_cloned = 'John',
                s_user_lastname_cloned = 'Doe',
        )
        """

    def testClonehistoryListElement(self):
        """Test ClonehistoryListElement"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
