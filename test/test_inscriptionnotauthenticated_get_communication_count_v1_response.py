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

from eZmaxApi.models.inscriptionnotauthenticated_get_communication_count_v1_response import InscriptionnotauthenticatedGetCommunicationCountV1Response

class TestInscriptionnotauthenticatedGetCommunicationCountV1Response(unittest.TestCase):
    """InscriptionnotauthenticatedGetCommunicationCountV1Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InscriptionnotauthenticatedGetCommunicationCountV1Response:
        """Test InscriptionnotauthenticatedGetCommunicationCountV1Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InscriptionnotauthenticatedGetCommunicationCountV1Response`
        """
        model = InscriptionnotauthenticatedGetCommunicationCountV1Response()
        if include_optional:
            return InscriptionnotauthenticatedGetCommunicationCountV1Response(
                m_payload = eZmaxApi.models.inscriptionnotauthenticated_get_communication_count_v1_response_m_payload.inscriptionnotauthenticated-getCommunicationCount-v1-Response-mPayload(
                    i_communication_count = 8, )
            )
        else:
            return InscriptionnotauthenticatedGetCommunicationCountV1Response(
                m_payload = eZmaxApi.models.inscriptionnotauthenticated_get_communication_count_v1_response_m_payload.inscriptionnotauthenticated-getCommunicationCount-v1-Response-mPayload(
                    i_communication_count = 8, ),
        )
        """

    def testInscriptionnotauthenticatedGetCommunicationCountV1Response(self):
        """Test InscriptionnotauthenticatedGetCommunicationCountV1Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
