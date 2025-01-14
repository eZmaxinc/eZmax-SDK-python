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

from eZmaxApi.models.ezsignelementdependency_request import EzsignelementdependencyRequest

class TestEzsignelementdependencyRequest(unittest.TestCase):
    """EzsignelementdependencyRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsignelementdependencyRequest:
        """Test EzsignelementdependencyRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsignelementdependencyRequest`
        """
        model = EzsignelementdependencyRequest()
        if include_optional:
            return EzsignelementdependencyRequest(
                pki_ezsignelementdependency_id = 89,
                fki_ezsignformfield_id_validation = 32,
                fki_ezsignformfieldgroup_id_validation = 26,
                s_ezsignelementdependency_ezsignformfieldgrouplabel = 'Allergies',
                s_ezsignelementdependency_ezsignformfieldlabel = 'Peanuts',
                e_ezsignelementdependency_validation = 'Value',
                b_ezsignelementdependency_selected = False,
                e_ezsignelementdependency_operator = 'eq',
                s_ezsignelementdependency_value = 'Montreal'
            )
        else:
            return EzsignelementdependencyRequest(
                e_ezsignelementdependency_validation = 'Value',
        )
        """

    def testEzsignelementdependencyRequest(self):
        """Test EzsignelementdependencyRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
