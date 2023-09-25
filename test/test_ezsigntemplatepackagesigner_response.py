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

from eZmaxApi.models.ezsigntemplatepackagesigner_response import EzsigntemplatepackagesignerResponse  # noqa: E501

class TestEzsigntemplatepackagesignerResponse(unittest.TestCase):
    """EzsigntemplatepackagesignerResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsigntemplatepackagesignerResponse:
        """Test EzsigntemplatepackagesignerResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsigntemplatepackagesignerResponse`
        """
        model = EzsigntemplatepackagesignerResponse()  # noqa: E501
        if include_optional:
            return EzsigntemplatepackagesignerResponse(
                pki_ezsigntemplatepackagesigner_id = 174,
                fki_ezsigntemplatepackage_id = 99,
                s_ezsigntemplatepackagesigner_description = 'Customer'
            )
        else:
            return EzsigntemplatepackagesignerResponse(
                pki_ezsigntemplatepackagesigner_id = 174,
                fki_ezsigntemplatepackage_id = 99,
                s_ezsigntemplatepackagesigner_description = 'Customer',
        )
        """

    def testEzsigntemplatepackagesignerResponse(self):
        """Test EzsigntemplatepackagesignerResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
