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

from eZmaxApi.models.rejectedoffertopurchase_get_communicationrecipients_v1_response import RejectedoffertopurchaseGetCommunicationrecipientsV1Response

class TestRejectedoffertopurchaseGetCommunicationrecipientsV1Response(unittest.TestCase):
    """RejectedoffertopurchaseGetCommunicationrecipientsV1Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RejectedoffertopurchaseGetCommunicationrecipientsV1Response:
        """Test RejectedoffertopurchaseGetCommunicationrecipientsV1Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RejectedoffertopurchaseGetCommunicationrecipientsV1Response`
        """
        model = RejectedoffertopurchaseGetCommunicationrecipientsV1Response()
        if include_optional:
            return RejectedoffertopurchaseGetCommunicationrecipientsV1Response(
                m_payload = eZmaxApi.models.rejectedoffertopurchase_get_communicationrecipients_v1_response_m_payload.rejectedoffertopurchase-getCommunicationrecipients-v1-Response-mPayload(
                    a_obj_communicationrecipientsgroup = [
                        eZmaxApi.models.custom_communicationrecipientsgroup_response.Custom-Communicationrecipientsgroup-Response(
                            s_communicationrecipientsgroup_label = '', 
                            a_obj_communicationrecipientsrecipient = [
                                eZmaxApi.models.custom_communicationrecipientsrecipient_response.Custom-Communicationrecipientsrecipient-Response(
                                    fki_agent_id = 1, 
                                    fki_broker_id = 26, 
                                    fki_contact_id = 21, 
                                    fki_customer_id = 18, 
                                    fki_employee_id = 31, 
                                    fki_ezsignsigner_id = 89, 
                                    fki_franchiseoffice_id = 50, 
                                    fki_user_id = 70, 
                                    fki_agentincorporation_id = 1, 
                                    fki_assistant_id = 1, 
                                    fki_externalbroker_id = 1, 
                                    fki_ezcomagent_id = 1, 
                                    fki_notary_id = 1, 
                                    fki_rewardmember_id = 1, 
                                    fki_supplier_id = 1, 
                                    e_communicationrecipientsrecipient_objecttype = 'User', 
                                    obj_contact_name = eZmaxApi.models.custom_contact_name_response.Custom-ContactName-Response(
                                        s_contact_firstname = 'John', 
                                        s_contact_lastname = 'Doe', 
                                        s_contact_company = 'eZmax Solutions Inc.', ), 
                                    obj_email = eZmaxApi.models.email_response_compound.email-ResponseCompound(), 
                                    obj_phone_fax = eZmaxApi.models.phone_response_compound.phone-ResponseCompound(), 
                                    obj_phone_sms = eZmaxApi.models.phone_response_compound.phone-ResponseCompound(), )
                                ], )
                        ], )
            )
        else:
            return RejectedoffertopurchaseGetCommunicationrecipientsV1Response(
                m_payload = eZmaxApi.models.rejectedoffertopurchase_get_communicationrecipients_v1_response_m_payload.rejectedoffertopurchase-getCommunicationrecipients-v1-Response-mPayload(
                    a_obj_communicationrecipientsgroup = [
                        eZmaxApi.models.custom_communicationrecipientsgroup_response.Custom-Communicationrecipientsgroup-Response(
                            s_communicationrecipientsgroup_label = '', 
                            a_obj_communicationrecipientsrecipient = [
                                eZmaxApi.models.custom_communicationrecipientsrecipient_response.Custom-Communicationrecipientsrecipient-Response(
                                    fki_agent_id = 1, 
                                    fki_broker_id = 26, 
                                    fki_contact_id = 21, 
                                    fki_customer_id = 18, 
                                    fki_employee_id = 31, 
                                    fki_ezsignsigner_id = 89, 
                                    fki_franchiseoffice_id = 50, 
                                    fki_user_id = 70, 
                                    fki_agentincorporation_id = 1, 
                                    fki_assistant_id = 1, 
                                    fki_externalbroker_id = 1, 
                                    fki_ezcomagent_id = 1, 
                                    fki_notary_id = 1, 
                                    fki_rewardmember_id = 1, 
                                    fki_supplier_id = 1, 
                                    e_communicationrecipientsrecipient_objecttype = 'User', 
                                    obj_contact_name = eZmaxApi.models.custom_contact_name_response.Custom-ContactName-Response(
                                        s_contact_firstname = 'John', 
                                        s_contact_lastname = 'Doe', 
                                        s_contact_company = 'eZmax Solutions Inc.', ), 
                                    obj_email = eZmaxApi.models.email_response_compound.email-ResponseCompound(), 
                                    obj_phone_fax = eZmaxApi.models.phone_response_compound.phone-ResponseCompound(), 
                                    obj_phone_sms = eZmaxApi.models.phone_response_compound.phone-ResponseCompound(), )
                                ], )
                        ], ),
        )
        """

    def testRejectedoffertopurchaseGetCommunicationrecipientsV1Response(self):
        """Test RejectedoffertopurchaseGetCommunicationrecipientsV1Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
