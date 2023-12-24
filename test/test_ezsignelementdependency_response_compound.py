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

from eZmaxApi.models.ezsignelementdependency_response_compound import EzsignelementdependencyResponseCompound

class TestEzsignelementdependencyResponseCompound(unittest.TestCase):
    """EzsignelementdependencyResponseCompound unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsignelementdependencyResponseCompound:
        """Test EzsignelementdependencyResponseCompound
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsignelementdependencyResponseCompound`
        """
        model = EzsignelementdependencyResponseCompound()
        if include_optional:
            return EzsignelementdependencyResponseCompound(
                pki_ezsignelementdependency_id = 89,
                fki_ezsignformfield_id = 32,
                fki_ezsignsignature_id = 49,
                fki_ezsignformfield_id_validation = 32,
                fki_ezsignformfieldgroup_id_validation = 26,
                e_ezsignelementdependency_validation = 'Value',
                b_ezsignelementdependency_selected = False,
                e_ezsignelementdependency_operator = 'eq',
                s_ezsignelementdependency_value = 'Montreal'
            )
        else:
            return EzsignelementdependencyResponseCompound(
                pki_ezsignelementdependency_id = 89,
                e_ezsignelementdependency_validation = 'Value',
        )
        """

    def testEzsignelementdependencyResponseCompound(self):
        """Test EzsignelementdependencyResponseCompound"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
