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

from eZmaxApi.models.rejectedoffertopurchase_get_communicationsenders_v1_response import RejectedoffertopurchaseGetCommunicationsendersV1Response

class TestRejectedoffertopurchaseGetCommunicationsendersV1Response(unittest.TestCase):
    """RejectedoffertopurchaseGetCommunicationsendersV1Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RejectedoffertopurchaseGetCommunicationsendersV1Response:
        """Test RejectedoffertopurchaseGetCommunicationsendersV1Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RejectedoffertopurchaseGetCommunicationsendersV1Response`
        """
        model = RejectedoffertopurchaseGetCommunicationsendersV1Response()
        if include_optional:
            return RejectedoffertopurchaseGetCommunicationsendersV1Response(
                obj_debug_payload = eZmaxApi.models.common_response_obj_debug_payload.Common-Response-objDebugPayload(
                    i_version_min = 1, 
                    i_version_max = 2, 
                    a_required_permission = [
                        117
                        ], 
                    b_version_deprecated = False, 
                    dt_response_date = '2020-12-31 23:59:59', ),
                obj_debug = {"sMemoryUsage":"11,923MB","sRunTime":"0.6084s","iSQLSelects":3,"iSQLQueries":6,"a_objSQLQuery":[{"sQuery":"SELECT * FROM table","fDuration":1.0E-4},{"sQuery":"SELECT * FROM table","fDuration":1.0E-4}]},
                m_payload = eZmaxApi.models.rejectedoffertopurchase_get_communicationsenders_v1_response_m_payload.rejectedoffertopurchase-getCommunicationsenders-v1-Response-mPayload(
                    a_obj_communicationsenders = [
                        eZmaxApi.models.custom_communicationsender_response.Custom-Communicationsender-Response(
                            fki_agent_id = 1, 
                            fki_broker_id = 26, 
                            fki_user_id = 70, 
                            fki_mailboxshared_id = 47, 
                            fki_phonelineshared_id = 47, 
                            e_communicationsender_objecttype = 'User', 
                            obj_contact_name = eZmaxApi.models.custom_contact_name_response.Custom-ContactName-Response(
                                s_contact_firstname = 'John', 
                                s_contact_lastname = 'Doe', 
                                s_contact_company = 'eZmax Solutions Inc.', ), 
                            obj_email = eZmaxApi.models.email_response_compound.email-ResponseCompound(), 
                            obj_phone_fax = eZmaxApi.models.phone_response_compound.phone-ResponseCompound(), 
                            obj_phone_sms = eZmaxApi.models.phone_response_compound.phone-ResponseCompound(), )
                        ], )
            )
        else:
            return RejectedoffertopurchaseGetCommunicationsendersV1Response(
                obj_debug_payload = eZmaxApi.models.common_response_obj_debug_payload.Common-Response-objDebugPayload(
                    i_version_min = 1, 
                    i_version_max = 2, 
                    a_required_permission = [
                        117
                        ], 
                    b_version_deprecated = False, 
                    dt_response_date = '2020-12-31 23:59:59', ),
                m_payload = eZmaxApi.models.rejectedoffertopurchase_get_communicationsenders_v1_response_m_payload.rejectedoffertopurchase-getCommunicationsenders-v1-Response-mPayload(
                    a_obj_communicationsenders = [
                        eZmaxApi.models.custom_communicationsender_response.Custom-Communicationsender-Response(
                            fki_agent_id = 1, 
                            fki_broker_id = 26, 
                            fki_user_id = 70, 
                            fki_mailboxshared_id = 47, 
                            fki_phonelineshared_id = 47, 
                            e_communicationsender_objecttype = 'User', 
                            obj_contact_name = eZmaxApi.models.custom_contact_name_response.Custom-ContactName-Response(
                                s_contact_firstname = 'John', 
                                s_contact_lastname = 'Doe', 
                                s_contact_company = 'eZmax Solutions Inc.', ), 
                            obj_email = eZmaxApi.models.email_response_compound.email-ResponseCompound(), 
                            obj_phone_fax = eZmaxApi.models.phone_response_compound.phone-ResponseCompound(), 
                            obj_phone_sms = eZmaxApi.models.phone_response_compound.phone-ResponseCompound(), )
                        ], ),
        )
        """

    def testRejectedoffertopurchaseGetCommunicationsendersV1Response(self):
        """Test RejectedoffertopurchaseGetCommunicationsendersV1Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
