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

from eZmaxApi.models.ezsigntemplateelementdependency_response import EzsigntemplateelementdependencyResponse  # noqa: E501

class TestEzsigntemplateelementdependencyResponse(unittest.TestCase):
    """EzsigntemplateelementdependencyResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsigntemplateelementdependencyResponse:
        """Test EzsigntemplateelementdependencyResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsigntemplateelementdependencyResponse`
        """
        model = EzsigntemplateelementdependencyResponse()  # noqa: E501
        if include_optional:
            return EzsigntemplateelementdependencyResponse(
                pki_ezsigntemplateelementdependency_id = 314,
                fki_ezsigntemplateformfield_id = 71,
                fki_ezsigntemplatesignature_id = 99,
                fki_ezsigntemplateformfield_id_validation = 71,
                fki_ezsigntemplateformfieldgroup_id_validation = 64,
                e_ezsigntemplateelementdependency_validation = 'Value',
                b_ezsigntemplateelementdependency_selected = False,
                e_ezsigntemplateelementdependency_operator = 'eq',
                s_ezsigntemplateelementdependency_value = 'Montreal'
            )
        else:
            return EzsigntemplateelementdependencyResponse(
                pki_ezsigntemplateelementdependency_id = 314,
                e_ezsigntemplateelementdependency_validation = 'Value',
        )
        """

    def testEzsigntemplateelementdependencyResponse(self):
        """Test EzsigntemplateelementdependencyResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
