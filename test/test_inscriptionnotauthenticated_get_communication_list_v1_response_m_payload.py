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

from eZmaxApi.models.inscriptionnotauthenticated_get_communication_list_v1_response_m_payload import InscriptionnotauthenticatedGetCommunicationListV1ResponseMPayload  # noqa: E501

class TestInscriptionnotauthenticatedGetCommunicationListV1ResponseMPayload(unittest.TestCase):
    """InscriptionnotauthenticatedGetCommunicationListV1ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InscriptionnotauthenticatedGetCommunicationListV1ResponseMPayload:
        """Test InscriptionnotauthenticatedGetCommunicationListV1ResponseMPayload
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InscriptionnotauthenticatedGetCommunicationListV1ResponseMPayload`
        """
        model = InscriptionnotauthenticatedGetCommunicationListV1ResponseMPayload()  # noqa: E501
        if include_optional:
            return InscriptionnotauthenticatedGetCommunicationListV1ResponseMPayload(
                a_obj_communication = [
                    eZmaxApi.models.custom_communication_list_element_response.Custom-CommunicationListElement-Response(
                        pki_communication_id = 1, 
                        dt_created_date = '2020-12-31 23:59:59', 
                        e_communication_direction = 'Outbound', 
                        e_communication_importance = 'Normal', 
                        e_communication_type = 'Email', 
                        i_communicationrecipient_count = 8, 
                        s_communication_subject = 'This is an example of subject', 
                        s_communication_sender = 'John Doe', 
                        s_communication_recipient = 'Jane Doe', )
                    ]
            )
        else:
            return InscriptionnotauthenticatedGetCommunicationListV1ResponseMPayload(
                a_obj_communication = [
                    eZmaxApi.models.custom_communication_list_element_response.Custom-CommunicationListElement-Response(
                        pki_communication_id = 1, 
                        dt_created_date = '2020-12-31 23:59:59', 
                        e_communication_direction = 'Outbound', 
                        e_communication_importance = 'Normal', 
                        e_communication_type = 'Email', 
                        i_communicationrecipient_count = 8, 
                        s_communication_subject = 'This is an example of subject', 
                        s_communication_sender = 'John Doe', 
                        s_communication_recipient = 'Jane Doe', )
                    ],
        )
        """

    def testInscriptionnotauthenticatedGetCommunicationListV1ResponseMPayload(self):
        """Test InscriptionnotauthenticatedGetCommunicationListV1ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
