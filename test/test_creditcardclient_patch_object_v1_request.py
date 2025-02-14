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

from eZmaxApi.models.creditcardclient_patch_object_v1_request import CreditcardclientPatchObjectV1Request

class TestCreditcardclientPatchObjectV1Request(unittest.TestCase):
    """CreditcardclientPatchObjectV1Request unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreditcardclientPatchObjectV1Request:
        """Test CreditcardclientPatchObjectV1Request
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreditcardclientPatchObjectV1Request`
        """
        model = CreditcardclientPatchObjectV1Request()
        if include_optional:
            return CreditcardclientPatchObjectV1Request(
                obj_creditcardclient = eZmaxApi.models.creditcardclient_request_patch.creditcardclient-RequestPatch(
                    b_creditcardclientrelation_isdefault = True, )
            )
        else:
            return CreditcardclientPatchObjectV1Request(
                obj_creditcardclient = eZmaxApi.models.creditcardclient_request_patch.creditcardclient-RequestPatch(
                    b_creditcardclientrelation_isdefault = True, ),
        )
        """

    def testCreditcardclientPatchObjectV1Request(self):
        """Test CreditcardclientPatchObjectV1Request"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
