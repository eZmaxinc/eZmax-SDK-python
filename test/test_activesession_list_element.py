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

from eZmaxApi.models.activesession_list_element import ActivesessionListElement

class TestActivesessionListElement(unittest.TestCase):
    """ActivesessionListElement unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ActivesessionListElement:
        """Test ActivesessionListElement
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ActivesessionListElement`
        """
        model = ActivesessionListElement()
        if include_optional:
            return ActivesessionListElement(
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
                s_activesession_ip = '127.0.0.1'
            )
        else:
            return ActivesessionListElement(
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
                s_activesession_ip = '127.0.0.1',
        )
        """

    def testActivesessionListElement(self):
        """Test ActivesessionListElement"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
