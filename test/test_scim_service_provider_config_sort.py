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
import datetime

from eZmaxApi.models.scim_service_provider_config_sort import ScimServiceProviderConfigSort  # noqa: E501

class TestScimServiceProviderConfigSort(unittest.TestCase):
    """ScimServiceProviderConfigSort unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ScimServiceProviderConfigSort:
        """Test ScimServiceProviderConfigSort
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ScimServiceProviderConfigSort`
        """
        model = ScimServiceProviderConfigSort()  # noqa: E501
        if include_optional:
            return ScimServiceProviderConfigSort(
                supported = False
            )
        else:
            return ScimServiceProviderConfigSort(
                supported = False,
        )
        """

    def testScimServiceProviderConfigSort(self):
        """Test ScimServiceProviderConfigSort"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
