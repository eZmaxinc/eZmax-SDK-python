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

from eZmaxApi.models.modulegroup_response_compound import ModulegroupResponseCompound

class TestModulegroupResponseCompound(unittest.TestCase):
    """ModulegroupResponseCompound unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ModulegroupResponseCompound:
        """Test ModulegroupResponseCompound
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ModulegroupResponseCompound`
        """
        model = ModulegroupResponseCompound()
        if include_optional:
            return ModulegroupResponseCompound(
                pki_modulegroup_id = 46,
                s_modulegroup_name_x = 'Management',
                a_obj_module = [
                    eZmaxApi.models.module_response_compound.module-ResponseCompound()
                    ]
            )
        else:
            return ModulegroupResponseCompound(
                pki_modulegroup_id = 46,
                s_modulegroup_name_x = 'Management',
        )
        """

    def testModulegroupResponseCompound(self):
        """Test ModulegroupResponseCompound"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
