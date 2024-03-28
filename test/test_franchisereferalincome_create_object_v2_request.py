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

from eZmaxApi.models.franchisereferalincome_create_object_v2_request import FranchisereferalincomeCreateObjectV2Request

class TestFranchisereferalincomeCreateObjectV2Request(unittest.TestCase):
    """FranchisereferalincomeCreateObjectV2Request unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FranchisereferalincomeCreateObjectV2Request:
        """Test FranchisereferalincomeCreateObjectV2Request
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FranchisereferalincomeCreateObjectV2Request`
        """
        model = FranchisereferalincomeCreateObjectV2Request()
        if include_optional:
            return FranchisereferalincomeCreateObjectV2Request(
                a_obj_franchisereferalincome = [
                    eZmaxApi.models.franchisereferalincome_request_compound.franchisereferalincome-RequestCompound()
                    ]
            )
        else:
            return FranchisereferalincomeCreateObjectV2Request(
                a_obj_franchisereferalincome = [
                    eZmaxApi.models.franchisereferalincome_request_compound.franchisereferalincome-RequestCompound()
                    ],
        )
        """

    def testFranchisereferalincomeCreateObjectV2Request(self):
        """Test FranchisereferalincomeCreateObjectV2Request"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
