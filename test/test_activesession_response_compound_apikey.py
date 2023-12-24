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

from eZmaxApi.models.activesession_response_compound_apikey import ActivesessionResponseCompoundApikey

class TestActivesessionResponseCompoundApikey(unittest.TestCase):
    """ActivesessionResponseCompoundApikey unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ActivesessionResponseCompoundApikey:
        """Test ActivesessionResponseCompoundApikey
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ActivesessionResponseCompoundApikey`
        """
        model = ActivesessionResponseCompoundApikey()
        if include_optional:
            return ActivesessionResponseCompoundApikey(
                pki_apikey_id = 99,
                s_apikey_description_x = 'Project X'
            )
        else:
            return ActivesessionResponseCompoundApikey(
                pki_apikey_id = 99,
                s_apikey_description_x = 'Project X',
        )
        """

    def testActivesessionResponseCompoundApikey(self):
        """Test ActivesessionResponseCompoundApikey"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
