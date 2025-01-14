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

from eZmaxApi.models.ezsigntemplateformfieldgroupsigner_response_compound import EzsigntemplateformfieldgroupsignerResponseCompound

class TestEzsigntemplateformfieldgroupsignerResponseCompound(unittest.TestCase):
    """EzsigntemplateformfieldgroupsignerResponseCompound unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsigntemplateformfieldgroupsignerResponseCompound:
        """Test EzsigntemplateformfieldgroupsignerResponseCompound
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsigntemplateformfieldgroupsignerResponseCompound`
        """
        model = EzsigntemplateformfieldgroupsignerResponseCompound()
        if include_optional:
            return EzsigntemplateformfieldgroupsignerResponseCompound(
                pki_ezsigntemplateformfieldgroupsigner_id = 87,
                fki_ezsigntemplatesigner_id = 9
            )
        else:
            return EzsigntemplateformfieldgroupsignerResponseCompound(
                pki_ezsigntemplateformfieldgroupsigner_id = 87,
                fki_ezsigntemplatesigner_id = 9,
        )
        """

    def testEzsigntemplateformfieldgroupsignerResponseCompound(self):
        """Test EzsigntemplateformfieldgroupsignerResponseCompound"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
