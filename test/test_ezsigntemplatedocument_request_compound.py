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

from eZmaxApi.models.ezsigntemplatedocument_request_compound import EzsigntemplatedocumentRequestCompound

class TestEzsigntemplatedocumentRequestCompound(unittest.TestCase):
    """EzsigntemplatedocumentRequestCompound unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsigntemplatedocumentRequestCompound:
        """Test EzsigntemplatedocumentRequestCompound
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsigntemplatedocumentRequestCompound`
        """
        model = EzsigntemplatedocumentRequestCompound()
        if include_optional:
            return EzsigntemplatedocumentRequestCompound(
                pki_ezsigntemplatedocument_id = 133,
                fki_ezsigntemplate_id = 36,
                fki_ezsigndocument_id = 97,
                fki_ezsigntemplatesigner_id = 9,
                s_ezsigntemplatedocument_name = 'Standard Contract',
                e_ezsigntemplatedocument_source = 'Base64',
                e_ezsigntemplatedocument_format = 'Pdf',
                s_ezsigntemplatedocument_base64 = 'eyIkcmVmIjoiIy9jb21wb25lbnRzL2V4YW1wbGVzL1BkZkFzQmFzZTY0L3ZhbHVlIn0=',
                s_ezsigntemplatedocument_url = 'http://www.example.com/template.pdf',
                b_ezsigntemplatedocument_forcerepair = True,
                e_ezsigntemplatedocument_form = 'Keep',
                s_ezsigntemplatedocument_password = ''
            )
        else:
            return EzsigntemplatedocumentRequestCompound(
                fki_ezsigntemplate_id = 36,
                s_ezsigntemplatedocument_name = 'Standard Contract',
                e_ezsigntemplatedocument_source = 'Base64',
        )
        """

    def testEzsigntemplatedocumentRequestCompound(self):
        """Test EzsigntemplatedocumentRequestCompound"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
