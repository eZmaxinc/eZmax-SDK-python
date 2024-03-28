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

from eZmaxApi.models.common_auditdetail import CommonAuditdetail

class TestCommonAuditdetail(unittest.TestCase):
    """CommonAuditdetail unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CommonAuditdetail:
        """Test CommonAuditdetail
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CommonAuditdetail`
        """
        model = CommonAuditdetail()
        if include_optional:
            return CommonAuditdetail(
                fki_user_id = 70,
                fki_apikey_id = 99,
                s_user_loginname = 'JohnDoe',
                s_user_lastname = 'Doe',
                s_user_firstname = 'John',
                s_apikey_description_x = 'Project X',
                dt_auditdetail_date = '2020-12-31 23:59:59'
            )
        else:
            return CommonAuditdetail(
                fki_user_id = 70,
                s_user_loginname = 'JohnDoe',
                s_user_lastname = 'Doe',
                s_user_firstname = 'John',
                dt_auditdetail_date = '2020-12-31 23:59:59',
        )
        """

    def testCommonAuditdetail(self):
        """Test CommonAuditdetail"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
