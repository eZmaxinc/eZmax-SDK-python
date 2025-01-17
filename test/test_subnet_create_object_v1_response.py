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

from eZmaxApi.models.subnet_create_object_v1_response import SubnetCreateObjectV1Response

class TestSubnetCreateObjectV1Response(unittest.TestCase):
    """SubnetCreateObjectV1Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SubnetCreateObjectV1Response:
        """Test SubnetCreateObjectV1Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SubnetCreateObjectV1Response`
        """
        model = SubnetCreateObjectV1Response()
        if include_optional:
            return SubnetCreateObjectV1Response(
                m_payload = eZmaxApi.models.subnet_create_object_v1_response_m_payload.subnet-createObject-v1-Response-mPayload(
                    a_pki_subnet_id = [
                        3
                        ], )
            )
        else:
            return SubnetCreateObjectV1Response(
                m_payload = eZmaxApi.models.subnet_create_object_v1_response_m_payload.subnet-createObject-v1-Response-mPayload(
                    a_pki_subnet_id = [
                        3
                        ], ),
        )
        """

    def testSubnetCreateObjectV1Response(self):
        """Test SubnetCreateObjectV1Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
