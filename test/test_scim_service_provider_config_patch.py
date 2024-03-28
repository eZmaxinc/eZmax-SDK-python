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

from eZmaxApi.models.scim_service_provider_config_patch import ScimServiceProviderConfigPatch

class TestScimServiceProviderConfigPatch(unittest.TestCase):
    """ScimServiceProviderConfigPatch unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ScimServiceProviderConfigPatch:
        """Test ScimServiceProviderConfigPatch
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ScimServiceProviderConfigPatch`
        """
        model = ScimServiceProviderConfigPatch()
        if include_optional:
            return ScimServiceProviderConfigPatch(
                supported = False
            )
        else:
            return ScimServiceProviderConfigPatch(
                supported = False,
        )
        """

    def testScimServiceProviderConfigPatch(self):
        """Test ScimServiceProviderConfigPatch"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
