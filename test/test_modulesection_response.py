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

from eZmaxApi.models.modulesection_response import ModulesectionResponse

class TestModulesectionResponse(unittest.TestCase):
    """ModulesectionResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ModulesectionResponse:
        """Test ModulesectionResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ModulesectionResponse`
        """
        model = ModulesectionResponse()
        if include_optional:
            return ModulesectionResponse(
                pki_modulesection_id = 53,
                fki_module_id = 40,
                s_modulesection_internalname = 'Access',
                s_modulesection_name_x = 'Access'
            )
        else:
            return ModulesectionResponse(
                pki_modulesection_id = 53,
                fki_module_id = 40,
                s_modulesection_internalname = 'Access',
                s_modulesection_name_x = 'Access',
        )
        """

    def testModulesectionResponse(self):
        """Test ModulesectionResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
