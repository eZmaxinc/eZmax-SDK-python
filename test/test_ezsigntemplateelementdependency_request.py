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

from eZmaxApi.models.ezsigntemplateelementdependency_request import EzsigntemplateelementdependencyRequest

class TestEzsigntemplateelementdependencyRequest(unittest.TestCase):
    """EzsigntemplateelementdependencyRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsigntemplateelementdependencyRequest:
        """Test EzsigntemplateelementdependencyRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsigntemplateelementdependencyRequest`
        """
        model = EzsigntemplateelementdependencyRequest()
        if include_optional:
            return EzsigntemplateelementdependencyRequest(
                pki_ezsigntemplateelementdependency_id = 314,
                fki_ezsigntemplateformfield_id_validation = 71,
                fki_ezsigntemplateformfieldgroup_id_validation = 64,
                s_ezsigntemplateelementdependency_ezsigntemplateformfieldgrouplabel = 'Allergies',
                s_ezsigntemplateelementdependency_ezsigntemplateformfieldlabel = 'Peanuts',
                e_ezsigntemplateelementdependency_validation = 'Value',
                b_ezsigntemplateelementdependency_selected = False,
                e_ezsigntemplateelementdependency_operator = 'eq',
                s_ezsigntemplateelementdependency_value = 'Montreal'
            )
        else:
            return EzsigntemplateelementdependencyRequest(
                e_ezsigntemplateelementdependency_validation = 'Value',
        )
        """

    def testEzsigntemplateelementdependencyRequest(self):
        """Test EzsigntemplateelementdependencyRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
