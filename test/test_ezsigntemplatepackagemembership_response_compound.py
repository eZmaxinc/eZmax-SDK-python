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

from eZmaxApi.models.ezsigntemplatepackagemembership_response_compound import EzsigntemplatepackagemembershipResponseCompound

class TestEzsigntemplatepackagemembershipResponseCompound(unittest.TestCase):
    """EzsigntemplatepackagemembershipResponseCompound unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsigntemplatepackagemembershipResponseCompound:
        """Test EzsigntemplatepackagemembershipResponseCompound
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsigntemplatepackagemembershipResponseCompound`
        """
        model = EzsigntemplatepackagemembershipResponseCompound()
        if include_optional:
            return EzsigntemplatepackagemembershipResponseCompound(
                pki_ezsigntemplatepackagemembership_id = 194,
                fki_ezsigntemplatepackage_id = 99,
                fki_ezsigntemplate_id = 36,
                i_ezsigntemplatepackagemembership_order = 1,
                obj_ezsigntemplate = eZmaxApi.models.ezsigntemplate_response_compound.ezsigntemplate-ResponseCompound(),
                a_obj_ezsigntemplatepackagesignermembership = [
                    eZmaxApi.models.ezsigntemplatepackagesignermembership_response_compound.ezsigntemplatepackagesignermembership-ResponseCompound()
                    ]
            )
        else:
            return EzsigntemplatepackagemembershipResponseCompound(
                pki_ezsigntemplatepackagemembership_id = 194,
                fki_ezsigntemplatepackage_id = 99,
                fki_ezsigntemplate_id = 36,
                i_ezsigntemplatepackagemembership_order = 1,
                obj_ezsigntemplate = eZmaxApi.models.ezsigntemplate_response_compound.ezsigntemplate-ResponseCompound(),
                a_obj_ezsigntemplatepackagesignermembership = [
                    eZmaxApi.models.ezsigntemplatepackagesignermembership_response_compound.ezsigntemplatepackagesignermembership-ResponseCompound()
                    ],
        )
        """

    def testEzsigntemplatepackagemembershipResponseCompound(self):
        """Test EzsigntemplatepackagemembershipResponseCompound"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
