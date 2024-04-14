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

from eZmaxApi.models.franchisereferalincome_create_object_v2_response_m_payload import FranchisereferalincomeCreateObjectV2ResponseMPayload

class TestFranchisereferalincomeCreateObjectV2ResponseMPayload(unittest.TestCase):
    """FranchisereferalincomeCreateObjectV2ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FranchisereferalincomeCreateObjectV2ResponseMPayload:
        """Test FranchisereferalincomeCreateObjectV2ResponseMPayload
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FranchisereferalincomeCreateObjectV2ResponseMPayload`
        """
        model = FranchisereferalincomeCreateObjectV2ResponseMPayload()
        if include_optional:
            return FranchisereferalincomeCreateObjectV2ResponseMPayload(
                a_pki_franchisereferalincome_id = [
                    35
                    ]
            )
        else:
            return FranchisereferalincomeCreateObjectV2ResponseMPayload(
                a_pki_franchisereferalincome_id = [
                    35
                    ],
        )
        """

    def testFranchisereferalincomeCreateObjectV2ResponseMPayload(self):
        """Test FranchisereferalincomeCreateObjectV2ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
