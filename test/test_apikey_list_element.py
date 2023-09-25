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

from eZmaxApi.models.apikey_list_element import ApikeyListElement  # noqa: E501

class TestApikeyListElement(unittest.TestCase):
    """ApikeyListElement unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApikeyListElement:
        """Test ApikeyListElement
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApikeyListElement`
        """
        model = ApikeyListElement()  # noqa: E501
        if include_optional:
            return ApikeyListElement(
                pki_apikey_id = 99,
                s_apikey_description_x = 'Project X',
                s_user_firstname = 'John',
                s_user_lastname = 'Doe',
                b_apikey_isactive = True,
                b_apikey_issigned = True
            )
        else:
            return ApikeyListElement(
                pki_apikey_id = 99,
                s_apikey_description_x = 'Project X',
                s_user_firstname = 'John',
                s_user_lastname = 'Doe',
                b_apikey_isactive = True,
                b_apikey_issigned = True,
        )
        """

    def testApikeyListElement(self):
        """Test ApikeyListElement"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
