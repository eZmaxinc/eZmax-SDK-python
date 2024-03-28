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

from eZmaxApi.models.ezsignbulksend_create_ezsignbulksendtransmission_v1_response_m_payload import EzsignbulksendCreateEzsignbulksendtransmissionV1ResponseMPayload

class TestEzsignbulksendCreateEzsignbulksendtransmissionV1ResponseMPayload(unittest.TestCase):
    """EzsignbulksendCreateEzsignbulksendtransmissionV1ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsignbulksendCreateEzsignbulksendtransmissionV1ResponseMPayload:
        """Test EzsignbulksendCreateEzsignbulksendtransmissionV1ResponseMPayload
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsignbulksendCreateEzsignbulksendtransmissionV1ResponseMPayload`
        """
        model = EzsignbulksendCreateEzsignbulksendtransmissionV1ResponseMPayload()
        if include_optional:
            return EzsignbulksendCreateEzsignbulksendtransmissionV1ResponseMPayload(
                obj_ezsignbulksendtransmission = eZmaxApi.models.ezsignbulksendtransmission_response.ezsignbulksendtransmission-Response(
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
                            dt_auditdetail_date = '2020-12-31 23:59:59', ), ), )
            )
        else:
            return EzsignbulksendCreateEzsignbulksendtransmissionV1ResponseMPayload(
                obj_ezsignbulksendtransmission = eZmaxApi.models.ezsignbulksendtransmission_response.ezsignbulksendtransmission-Response(
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
                            dt_auditdetail_date = '2020-12-31 23:59:59', ), ), ),
        )
        """

    def testEzsignbulksendCreateEzsignbulksendtransmissionV1ResponseMPayload(self):
        """Test EzsignbulksendCreateEzsignbulksendtransmissionV1ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
