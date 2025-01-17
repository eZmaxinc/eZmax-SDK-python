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

from eZmaxApi.models.ezsignbulksend_create_ezsignbulksendtransmission_v2_response import EzsignbulksendCreateEzsignbulksendtransmissionV2Response

class TestEzsignbulksendCreateEzsignbulksendtransmissionV2Response(unittest.TestCase):
    """EzsignbulksendCreateEzsignbulksendtransmissionV2Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsignbulksendCreateEzsignbulksendtransmissionV2Response:
        """Test EzsignbulksendCreateEzsignbulksendtransmissionV2Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsignbulksendCreateEzsignbulksendtransmissionV2Response`
        """
        model = EzsignbulksendCreateEzsignbulksendtransmissionV2Response()
        if include_optional:
            return EzsignbulksendCreateEzsignbulksendtransmissionV2Response(
                obj_debug_payload = eZmaxApi.models.common_response_obj_debug_payload.Common-Response-objDebugPayload(
                    i_version_min = 1, 
                    i_version_max = 2, 
                    a_required_permission = [
                        117
                        ], 
                    b_version_deprecated = False, 
                    dt_response_date = '2020-12-31 23:59:59', ),
                obj_debug = {"sMemoryUsage":"11,923MB","sRunTime":"0.6084s","iSQLSelects":3,"iSQLQueries":6,"a_objSQLQuery":[{"sQuery":"SELECT * FROM table","fDuration":1.0E-4},{"sQuery":"SELECT * FROM table","fDuration":1.0E-4}]},
                m_payload = eZmaxApi.models.ezsignbulksend_create_ezsignbulksendtransmission_v2_response_m_payload.ezsignbulksend-createEzsignbulksendtransmission-v2-Response-mPayload(
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
                                dt_auditdetail_date = '2020-12-31 23:59:59', ), ), ), )
            )
        else:
            return EzsignbulksendCreateEzsignbulksendtransmissionV2Response(
                obj_debug_payload = eZmaxApi.models.common_response_obj_debug_payload.Common-Response-objDebugPayload(
                    i_version_min = 1, 
                    i_version_max = 2, 
                    a_required_permission = [
                        117
                        ], 
                    b_version_deprecated = False, 
                    dt_response_date = '2020-12-31 23:59:59', ),
                m_payload = eZmaxApi.models.ezsignbulksend_create_ezsignbulksendtransmission_v2_response_m_payload.ezsignbulksend-createEzsignbulksendtransmission-v2-Response-mPayload(
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
                                dt_auditdetail_date = '2020-12-31 23:59:59', ), ), ), ),
        )
        """

    def testEzsignbulksendCreateEzsignbulksendtransmissionV2Response(self):
        """Test EzsignbulksendCreateEzsignbulksendtransmissionV2Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
