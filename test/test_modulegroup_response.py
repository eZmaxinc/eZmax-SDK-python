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

from eZmaxApi.models.modulegroup_response import ModulegroupResponse

class TestModulegroupResponse(unittest.TestCase):
    """ModulegroupResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ModulegroupResponse:
        """Test ModulegroupResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ModulegroupResponse`
        """
        model = ModulegroupResponse()
        if include_optional:
            return ModulegroupResponse(
                pki_modulegroup_id = 46,
                s_modulegroup_name_x = 'Management'
            )
        else:
            return ModulegroupResponse(
                pki_modulegroup_id = 46,
                s_modulegroup_name_x = 'Management',
        )
        """

    def testModulegroupResponse(self):
        """Test ModulegroupResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
