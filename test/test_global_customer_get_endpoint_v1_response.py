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

from eZmaxApi.models.global_customer_get_endpoint_v1_response import GlobalCustomerGetEndpointV1Response

class TestGlobalCustomerGetEndpointV1Response(unittest.TestCase):
    """GlobalCustomerGetEndpointV1Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GlobalCustomerGetEndpointV1Response:
        """Test GlobalCustomerGetEndpointV1Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GlobalCustomerGetEndpointV1Response`
        """
        model = GlobalCustomerGetEndpointV1Response()
        if include_optional:
            return GlobalCustomerGetEndpointV1Response(
                s_endpoint_url = ''
            )
        else:
            return GlobalCustomerGetEndpointV1Response(
                s_endpoint_url = '',
        )
        """

    def testGlobalCustomerGetEndpointV1Response(self):
        """Test GlobalCustomerGetEndpointV1Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
