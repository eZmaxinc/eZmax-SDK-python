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

from eZmaxApi.models.ezsigntemplatedocument_request import EzsigntemplatedocumentRequest

class TestEzsigntemplatedocumentRequest(unittest.TestCase):
    """EzsigntemplatedocumentRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsigntemplatedocumentRequest:
        """Test EzsigntemplatedocumentRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsigntemplatedocumentRequest`
        """
        model = EzsigntemplatedocumentRequest()
        if include_optional:
            return EzsigntemplatedocumentRequest(
                pki_ezsigntemplatedocument_id = 133,
                fki_ezsigntemplate_id = 36,
                fki_ezsigndocument_id = 97,
                fki_ezsigntemplatesigner_id = 9,
                s_ezsigntemplatedocument_name = 'Standard Contract',
                e_ezsigntemplatedocument_source = 'Base64',
                e_ezsigntemplatedocument_format = 'Pdf',
                s_ezsigntemplatedocument_base64 = '[B@59fc684e',
                s_ezsigntemplatedocument_url = 'http://www.example.com/template.pdf',
                b_ezsigntemplatedocument_forcerepair = True,
                e_ezsigntemplatedocument_form = 'Keep',
                s_ezsigntemplatedocument_password = ''
            )
        else:
            return EzsigntemplatedocumentRequest(
                fki_ezsigntemplate_id = 36,
                s_ezsigntemplatedocument_name = 'Standard Contract',
                e_ezsigntemplatedocument_source = 'Base64',
        )
        """

    def testEzsigntemplatedocumentRequest(self):
        """Test EzsigntemplatedocumentRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
