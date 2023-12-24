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

from eZmaxApi.models.ezsigndocumentlog_response import EzsigndocumentlogResponse

class TestEzsigndocumentlogResponse(unittest.TestCase):
    """EzsigndocumentlogResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsigndocumentlogResponse:
        """Test EzsigndocumentlogResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsigndocumentlogResponse`
        """
        model = EzsigndocumentlogResponse()
        if include_optional:
            return EzsigndocumentlogResponse(
                fki_user_id = 70,
                fki_ezsignsigner_id = 89,
                dt_ezsigndocumentlog_datetime = '2020-12-31 23:59:59',
                e_ezsigndocumentlog_type = 'Createpage',
                s_ezsigndocumentlog_detail = 'Page 1 MD5: a56bbc742ba2a4d074f2493550cf6ea5',
                s_ezsigndocumentlog_lastname = 'Doe',
                s_ezsigndocumentlog_firstname = 'John',
                s_ezsigndocumentlog_ip = '127.0.0.1'
            )
        else:
            return EzsigndocumentlogResponse(
                dt_ezsigndocumentlog_datetime = '2020-12-31 23:59:59',
                e_ezsigndocumentlog_type = 'Createpage',
                s_ezsigndocumentlog_detail = 'Page 1 MD5: a56bbc742ba2a4d074f2493550cf6ea5',
                s_ezsigndocumentlog_lastname = 'Doe',
                s_ezsigndocumentlog_firstname = 'John',
                s_ezsigndocumentlog_ip = '127.0.0.1',
        )
        """

    def testEzsigndocumentlogResponse(self):
        """Test EzsigndocumentlogResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
