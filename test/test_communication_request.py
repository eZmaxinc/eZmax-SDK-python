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

from eZmaxApi.models.communication_request import CommunicationRequest

class TestCommunicationRequest(unittest.TestCase):
    """CommunicationRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CommunicationRequest:
        """Test CommunicationRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CommunicationRequest`
        """
        model = CommunicationRequest()
        if include_optional:
            return CommunicationRequest(
                pki_communication_id = 1,
                e_communication_importance = 'Normal',
                e_communication_type = 'Email',
                obj_communicationsender = eZmaxApi.models.custom_communicationsender_request.Custom-Communicationsender-Request(
                    fki_agent_id = 1, 
                    fki_broker_id = 26, 
                    fki_mailboxshared_id = 47, 
                    fki_phonelineshared_id = 47, 
                    fki_user_id = 70, ),
                s_communication_subject = 'This is an example of subject',
                t_communication_body = '',
                b_communication_private = False,
                e_communication_attachmenttype = 'Attachment',
                i_communication_attachmentlinkexpiration = 1,
                b_communication_readreceipt = True
            )
        else:
            return CommunicationRequest(
                e_communication_type = 'Email',
                t_communication_body = '',
                b_communication_private = False,
        )
        """

    def testCommunicationRequest(self):
        """Test CommunicationRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()