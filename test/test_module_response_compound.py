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

from eZmaxApi.models.module_response_compound import ModuleResponseCompound

class TestModuleResponseCompound(unittest.TestCase):
    """ModuleResponseCompound unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ModuleResponseCompound:
        """Test ModuleResponseCompound
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ModuleResponseCompound`
        """
        model = ModuleResponseCompound()
        if include_optional:
            return ModuleResponseCompound(
                pki_module_id = 40,
                fki_modulegroup_id = 46,
                e_module_internalname = 'Purchases',
                s_module_name_x = 'Purchase',
                b_module_registered = True,
                b_module_registeredapi = True,
                a_obj_modulesection = [
                    eZmaxApi.models.modulesection_response_compound.modulesection-ResponseCompound()
                    ]
            )
        else:
            return ModuleResponseCompound(
                pki_module_id = 40,
                fki_modulegroup_id = 46,
                e_module_internalname = 'Purchases',
                s_module_name_x = 'Purchase',
                b_module_registered = True,
                b_module_registeredapi = True,
        )
        """

    def testModuleResponseCompound(self):
        """Test ModuleResponseCompound"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
