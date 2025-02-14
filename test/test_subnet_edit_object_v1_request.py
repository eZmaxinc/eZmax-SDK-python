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

from eZmaxApi.models.subnet_edit_object_v1_request import SubnetEditObjectV1Request

class TestSubnetEditObjectV1Request(unittest.TestCase):
    """SubnetEditObjectV1Request unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SubnetEditObjectV1Request:
        """Test SubnetEditObjectV1Request
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SubnetEditObjectV1Request`
        """
        model = SubnetEditObjectV1Request()
        if include_optional:
            return SubnetEditObjectV1Request(
                obj_subnet = eZmaxApi.models.subnet_request_compound.subnet-RequestCompound()
            )
        else:
            return SubnetEditObjectV1Request(
                obj_subnet = eZmaxApi.models.subnet_request_compound.subnet-RequestCompound(),
        )
        """

    def testSubnetEditObjectV1Request(self):
        """Test SubnetEditObjectV1Request"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
