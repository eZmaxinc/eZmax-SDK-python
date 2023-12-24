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

from eZmaxApi.models.ezsigntemplatepackage_response import EzsigntemplatepackageResponse

class TestEzsigntemplatepackageResponse(unittest.TestCase):
    """EzsigntemplatepackageResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsigntemplatepackageResponse:
        """Test EzsigntemplatepackageResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsigntemplatepackageResponse`
        """
        model = EzsigntemplatepackageResponse()
        if include_optional:
            return EzsigntemplatepackageResponse(
                pki_ezsigntemplatepackage_id = 99,
                fki_ezsignfoldertype_id = 5,
                fki_language_id = 2,
                s_language_name_x = 'English',
                s_ezsigntemplatepackage_description = 'Package for new clients',
                b_ezsigntemplatepackage_adminonly = True,
                b_ezsigntemplatepackage_needvalidation = True,
                b_ezsigntemplatepackage_isactive = True,
                s_ezsignfoldertype_name_x = 'Default'
            )
        else:
            return EzsigntemplatepackageResponse(
                pki_ezsigntemplatepackage_id = 99,
                fki_ezsignfoldertype_id = 5,
                fki_language_id = 2,
                s_language_name_x = 'English',
                s_ezsigntemplatepackage_description = 'Package for new clients',
                b_ezsigntemplatepackage_adminonly = True,
                b_ezsigntemplatepackage_needvalidation = True,
                b_ezsigntemplatepackage_isactive = True,
                s_ezsignfoldertype_name_x = 'Default',
        )
        """

    def testEzsigntemplatepackageResponse(self):
        """Test EzsigntemplatepackageResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
