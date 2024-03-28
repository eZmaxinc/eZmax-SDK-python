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

from eZmaxApi.models.usergroupexternal_list_element import UsergroupexternalListElement

class TestUsergroupexternalListElement(unittest.TestCase):
    """UsergroupexternalListElement unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UsergroupexternalListElement:
        """Test UsergroupexternalListElement
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UsergroupexternalListElement`
        """
        model = UsergroupexternalListElement()
        if include_optional:
            return UsergroupexternalListElement(
                pki_usergroupexternal_id = 16,
                s_usergroupexternal_name = 'Administrators',
                s_usergroupexternal_id = '5140-1542'
            )
        else:
            return UsergroupexternalListElement(
                pki_usergroupexternal_id = 16,
                s_usergroupexternal_name = 'Administrators',
                s_usergroupexternal_id = '5140-1542',
        )
        """

    def testUsergroupexternalListElement(self):
        """Test UsergroupexternalListElement"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
