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

from eZmaxApi.models.ezsigntemplatepackagesignermembership_response import EzsigntemplatepackagesignermembershipResponse

class TestEzsigntemplatepackagesignermembershipResponse(unittest.TestCase):
    """EzsigntemplatepackagesignermembershipResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsigntemplatepackagesignermembershipResponse:
        """Test EzsigntemplatepackagesignermembershipResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsigntemplatepackagesignermembershipResponse`
        """
        model = EzsigntemplatepackagesignermembershipResponse()
        if include_optional:
            return EzsigntemplatepackagesignermembershipResponse(
                pki_ezsigntemplatepackagesignermembership_id = 237,
                fki_ezsigntemplatepackagemembership_id = 194,
                fki_ezsigntemplatepackagesigner_id = 174,
                fki_ezsigntemplatesigner_id = 9,
                i_ezsigntemplatepackagesignermembership_copy = 1
            )
        else:
            return EzsigntemplatepackagesignermembershipResponse(
                pki_ezsigntemplatepackagesignermembership_id = 237,
                fki_ezsigntemplatepackagemembership_id = 194,
                fki_ezsigntemplatepackagesigner_id = 174,
                fki_ezsigntemplatesigner_id = 9,
        )
        """

    def testEzsigntemplatepackagesignermembershipResponse(self):
        """Test EzsigntemplatepackagesignermembershipResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
