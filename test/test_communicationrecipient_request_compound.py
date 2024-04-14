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

from eZmaxApi.models.communicationrecipient_request_compound import CommunicationrecipientRequestCompound

class TestCommunicationrecipientRequestCompound(unittest.TestCase):
    """CommunicationrecipientRequestCompound unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CommunicationrecipientRequestCompound:
        """Test CommunicationrecipientRequestCompound
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CommunicationrecipientRequestCompound`
        """
        model = CommunicationrecipientRequestCompound()
        if include_optional:
            return CommunicationrecipientRequestCompound(
                pki_communicationrecipient_id = 1,
                fki_agent_id = 1,
                fki_broker_id = 26,
                fki_contact_id = 21,
                fki_customer_id = 18,
                fki_employee_id = 31,
                fki_assistant_id = 1,
                fki_externalbroker_id = 1,
                fki_ezsignsigner_id = 89,
                fki_notary_id = 1,
                fki_supplier_id = 1,
                fki_user_id = 70,
                fki_mailboxshared_id = 47,
                fki_phonelineshared_id = 47,
                e_communicationrecipient_type = 'To'
            )
        else:
            return CommunicationrecipientRequestCompound(
        )
        """

    def testCommunicationrecipientRequestCompound(self):
        """Test CommunicationrecipientRequestCompound"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
