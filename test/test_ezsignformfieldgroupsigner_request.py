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

from eZmaxApi.models.ezsignformfieldgroupsigner_request import EzsignformfieldgroupsignerRequest

class TestEzsignformfieldgroupsignerRequest(unittest.TestCase):
    """EzsignformfieldgroupsignerRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsignformfieldgroupsignerRequest:
        """Test EzsignformfieldgroupsignerRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsignformfieldgroupsignerRequest`
        """
        model = EzsignformfieldgroupsignerRequest()
        if include_optional:
            return EzsignformfieldgroupsignerRequest(
                pki_ezsignformfieldgroupsigner_id = 81,
                fki_ezsignfoldersignerassociation_id = 20
            )
        else:
            return EzsignformfieldgroupsignerRequest(
                fki_ezsignfoldersignerassociation_id = 20,
        )
        """

    def testEzsignformfieldgroupsignerRequest(self):
        """Test EzsignformfieldgroupsignerRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
