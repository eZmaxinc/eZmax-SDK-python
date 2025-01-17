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

from eZmaxApi.models.otherincome_get_communicationsenders_v1_response import OtherincomeGetCommunicationsendersV1Response

class TestOtherincomeGetCommunicationsendersV1Response(unittest.TestCase):
    """OtherincomeGetCommunicationsendersV1Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OtherincomeGetCommunicationsendersV1Response:
        """Test OtherincomeGetCommunicationsendersV1Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OtherincomeGetCommunicationsendersV1Response`
        """
        model = OtherincomeGetCommunicationsendersV1Response()
        if include_optional:
            return OtherincomeGetCommunicationsendersV1Response(
                m_payload = eZmaxApi.models.otherincome_get_communicationsenders_v1_response_m_payload.otherincome-getCommunicationsenders-v1-Response-mPayload(
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
            return OtherincomeGetCommunicationsendersV1Response(
                m_payload = eZmaxApi.models.otherincome_get_communicationsenders_v1_response_m_payload.otherincome-getCommunicationsenders-v1-Response-mPayload(
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

    def testOtherincomeGetCommunicationsendersV1Response(self):
        """Test OtherincomeGetCommunicationsendersV1Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
