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

from eZmaxApi.models.ezsignbulksenddocumentmapping_response import EzsignbulksenddocumentmappingResponse

class TestEzsignbulksenddocumentmappingResponse(unittest.TestCase):
    """EzsignbulksenddocumentmappingResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsignbulksenddocumentmappingResponse:
        """Test EzsignbulksenddocumentmappingResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsignbulksenddocumentmappingResponse`
        """
        model = EzsignbulksenddocumentmappingResponse()
        if include_optional:
            return EzsignbulksenddocumentmappingResponse(
                pki_ezsignbulksenddocumentmapping_id = 48,
                fki_ezsignbulksend_id = 8,
                fki_ezsigntemplatepackage_id = 99,
                fki_ezsigntemplate_id = 36,
                i_ezsignbulksenddocumentmapping_order = 1
            )
        else:
            return EzsignbulksenddocumentmappingResponse(
                pki_ezsignbulksenddocumentmapping_id = 48,
                fki_ezsignbulksend_id = 8,
                i_ezsignbulksenddocumentmapping_order = 1,
        )
        """

    def testEzsignbulksenddocumentmappingResponse(self):
        """Test EzsignbulksenddocumentmappingResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
