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

from eZmaxApi.models.usergroup_request_compound import UsergroupRequestCompound

class TestUsergroupRequestCompound(unittest.TestCase):
    """UsergroupRequestCompound unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UsergroupRequestCompound:
        """Test UsergroupRequestCompound
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UsergroupRequestCompound`
        """
        model = UsergroupRequestCompound()
        if include_optional:
            return UsergroupRequestCompound(
                pki_usergroup_id = 2,
                obj_usergroup_name = eZmaxApi.models.multilingual_usergroup_name.Multilingual-UsergroupName(
                    s_usergroup_name1 = 'Direction', 
                    s_usergroup_name2 = 'Management', )
            )
        else:
            return UsergroupRequestCompound(
                obj_usergroup_name = eZmaxApi.models.multilingual_usergroup_name.Multilingual-UsergroupName(
                    s_usergroup_name1 = 'Direction', 
                    s_usergroup_name2 = 'Management', ),
        )
        """

    def testUsergroupRequestCompound(self):
        """Test UsergroupRequestCompound"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
