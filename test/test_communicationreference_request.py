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

from eZmaxApi.models.communicationreference_request import CommunicationreferenceRequest

class TestCommunicationreferenceRequest(unittest.TestCase):
    """CommunicationreferenceRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CommunicationreferenceRequest:
        """Test CommunicationreferenceRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CommunicationreferenceRequest`
        """
        model = CommunicationreferenceRequest()
        if include_optional:
            return CommunicationreferenceRequest(
                pki_communicationreference_id = 1263,
                fki_buyercontract_id = 38,
                fki_ezsignfolder_id = 33,
                fki_inscription_id = 17,
                fki_inscriptiontemp_id = 2445,
                fki_invoice_id = 1,
                fki_otherincome_id = 142,
                fki_electronicfundstransfer_id = 1262,
                fki_rejectedoffertopurchase_id = 532
            )
        else:
            return CommunicationreferenceRequest(
        )
        """

    def testCommunicationreferenceRequest(self):
        """Test CommunicationreferenceRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
