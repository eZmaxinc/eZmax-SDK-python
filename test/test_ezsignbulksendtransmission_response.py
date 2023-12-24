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

from eZmaxApi.models.ezsignbulksendtransmission_response import EzsignbulksendtransmissionResponse

class TestEzsignbulksendtransmissionResponse(unittest.TestCase):
    """EzsignbulksendtransmissionResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsignbulksendtransmissionResponse:
        """Test EzsignbulksendtransmissionResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsignbulksendtransmissionResponse`
        """
        model = EzsignbulksendtransmissionResponse()
        if include_optional:
            return EzsignbulksendtransmissionResponse(
                pki_ezsignbulksendtransmission_id = 21,
                fki_ezsignbulksend_id = 8,
                s_ezsignbulksendtransmission_description = 'Test eZsign Bulk Send Transmission #1',
                i_ezsignbulksendtransmission_errors = 1,
                obj_audit = eZmaxApi.models.common_audit.Common-Audit(
                    obj_auditdetail_created = eZmaxApi.models.common_auditdetail.Common-Auditdetail(
                        fki_user_id = 70, 
                        fki_apikey_id = 99, 
                        s_user_loginname = 'JohnDoe', 
                        s_user_lastname = 'Doe', 
                        s_user_firstname = 'John', 
                        s_apikey_description_x = 'Project X', 
                        dt_auditdetail_date = '2020-12-31 23:59:59', ), 
                    obj_auditdetail_modified = eZmaxApi.models.common_auditdetail.Common-Auditdetail(
                        fki_user_id = 70, 
                        fki_apikey_id = 99, 
                        s_user_loginname = 'JohnDoe', 
                        s_user_lastname = 'Doe', 
                        s_user_firstname = 'John', 
                        s_apikey_description_x = 'Project X', 
                        dt_auditdetail_date = '2020-12-31 23:59:59', ), )
            )
        else:
            return EzsignbulksendtransmissionResponse(
                pki_ezsignbulksendtransmission_id = 21,
                fki_ezsignbulksend_id = 8,
                s_ezsignbulksendtransmission_description = 'Test eZsign Bulk Send Transmission #1',
                i_ezsignbulksendtransmission_errors = 1,
                obj_audit = eZmaxApi.models.common_audit.Common-Audit(
                    obj_auditdetail_created = eZmaxApi.models.common_auditdetail.Common-Auditdetail(
                        fki_user_id = 70, 
                        fki_apikey_id = 99, 
                        s_user_loginname = 'JohnDoe', 
                        s_user_lastname = 'Doe', 
                        s_user_firstname = 'John', 
                        s_apikey_description_x = 'Project X', 
                        dt_auditdetail_date = '2020-12-31 23:59:59', ), 
                    obj_auditdetail_modified = eZmaxApi.models.common_auditdetail.Common-Auditdetail(
                        fki_user_id = 70, 
                        fki_apikey_id = 99, 
                        s_user_loginname = 'JohnDoe', 
                        s_user_lastname = 'Doe', 
                        s_user_firstname = 'John', 
                        s_apikey_description_x = 'Project X', 
                        dt_auditdetail_date = '2020-12-31 23:59:59', ), ),
        )
        """

    def testEzsignbulksendtransmissionResponse(self):
        """Test EzsignbulksendtransmissionResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
