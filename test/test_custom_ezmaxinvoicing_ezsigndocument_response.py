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

from eZmaxApi.models.custom_ezmaxinvoicing_ezsigndocument_response import CustomEzmaxinvoicingEzsigndocumentResponse

class TestCustomEzmaxinvoicingEzsigndocumentResponse(unittest.TestCase):
    """CustomEzmaxinvoicingEzsigndocumentResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CustomEzmaxinvoicingEzsigndocumentResponse:
        """Test CustomEzmaxinvoicingEzsigndocumentResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CustomEzmaxinvoicingEzsigndocumentResponse`
        """
        model = CustomEzmaxinvoicingEzsigndocumentResponse()
        if include_optional:
            return CustomEzmaxinvoicingEzsigndocumentResponse(
                fki_ezsignfolder_id = 33,
                fki_billingentityinternal_id = 1,
                s_name = '',
                s_ezsignfolder_description = 'Test eZsign Folder',
                s_ezsigndocument_name = 'Contract #123',
                b_ezsignfolder_allowed = True
            )
        else:
            return CustomEzmaxinvoicingEzsigndocumentResponse(
                fki_ezsignfolder_id = 33,
                s_name = '',
                s_ezsignfolder_description = 'Test eZsign Folder',
                s_ezsigndocument_name = 'Contract #123',
                b_ezsignfolder_allowed = True,
        )
        """

    def testCustomEzmaxinvoicingEzsigndocumentResponse(self):
        """Test CustomEzmaxinvoicingEzsigndocumentResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
