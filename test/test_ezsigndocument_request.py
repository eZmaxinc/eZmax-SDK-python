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

from eZmaxApi.models.ezsigndocument_request import EzsigndocumentRequest

class TestEzsigndocumentRequest(unittest.TestCase):
    """EzsigndocumentRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsigndocumentRequest:
        """Test EzsigndocumentRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsigndocumentRequest`
        """
        model = EzsigndocumentRequest()
        if include_optional:
            return EzsigndocumentRequest(
                pki_ezsigndocument_id = 97,
                fki_ezsignfolder_id = 33,
                fki_ezsigntemplate_id = 36,
                fki_ezsignfoldersignerassociation_id = 20,
                fki_language_id = 2,
                e_ezsigndocument_source = 'Base64',
                e_ezsigndocument_format = 'Pdf',
                s_ezsigndocument_base64 = '[B@172ca72b',
                s_ezsigndocument_url = 'http://www.example.com/document.pdf',
                b_ezsigndocument_forcerepair = True,
                s_ezsigndocument_password = 'SecretPassword123',
                e_ezsigndocument_form = 'Keep',
                dt_ezsigndocument_duedate = '2020-12-31 23:59:59',
                s_ezsigndocument_name = 'Contract #123',
                s_ezsigndocument_externalid = '{"ID": 1234, "TAGS": ["tag1", "tag2", "tag3"]}'
            )
        else:
            return EzsigndocumentRequest(
                fki_ezsignfolder_id = 33,
                fki_language_id = 2,
                e_ezsigndocument_source = 'Base64',
                dt_ezsigndocument_duedate = '2020-12-31 23:59:59',
                s_ezsigndocument_name = 'Contract #123',
        )
        """

    def testEzsigndocumentRequest(self):
        """Test EzsigndocumentRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
