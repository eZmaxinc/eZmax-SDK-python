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

from eZmaxApi.models.electronicfundstransfer_get_communication_count_v1_response import ElectronicfundstransferGetCommunicationCountV1Response

class TestElectronicfundstransferGetCommunicationCountV1Response(unittest.TestCase):
    """ElectronicfundstransferGetCommunicationCountV1Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ElectronicfundstransferGetCommunicationCountV1Response:
        """Test ElectronicfundstransferGetCommunicationCountV1Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ElectronicfundstransferGetCommunicationCountV1Response`
        """
        model = ElectronicfundstransferGetCommunicationCountV1Response()
        if include_optional:
            return ElectronicfundstransferGetCommunicationCountV1Response(
                m_payload = eZmaxApi.models.electronicfundstransfer_get_communication_count_v1_response_m_payload.electronicfundstransfer-getCommunicationCount-v1-Response-mPayload(
                    i_communication_count = 8, )
            )
        else:
            return ElectronicfundstransferGetCommunicationCountV1Response(
                m_payload = eZmaxApi.models.electronicfundstransfer_get_communication_count_v1_response_m_payload.electronicfundstransfer-getCommunicationCount-v1-Response-mPayload(
                    i_communication_count = 8, ),
        )
        """

    def testElectronicfundstransferGetCommunicationCountV1Response(self):
        """Test ElectronicfundstransferGetCommunicationCountV1Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
