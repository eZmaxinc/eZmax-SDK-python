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

from eZmaxApi.models.ezsigndocument_request_compound import EzsigndocumentRequestCompound

class TestEzsigndocumentRequestCompound(unittest.TestCase):
    """EzsigndocumentRequestCompound unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsigndocumentRequestCompound:
        """Test EzsigndocumentRequestCompound
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsigndocumentRequestCompound`
        """
        model = EzsigndocumentRequestCompound()
        if include_optional:
            return EzsigndocumentRequestCompound(
                pki_ezsigndocument_id = 97,
                fki_ezsignfolder_id = 33,
                fki_ezsigntemplate_id = 36,
                fki_ezsignfoldersignerassociation_id = 20,
                fki_language_id = 2,
                e_ezsigndocument_source = 'Base64',
                e_ezsigndocument_format = 'Pdf',
                s_ezsigndocument_base64 = 'eyIkcmVmIjoiIy9jb21wb25lbnRzL2V4YW1wbGVzL1BkZkFzQmFzZTY0L3ZhbHVlIn0=',
                s_ezsigndocument_url = 'http://www.example.com/document.pdf',
                b_ezsigndocument_forcerepair = True,
                s_ezsigndocument_password = 'SecretPassword123',
                e_ezsigndocument_form = 'Keep',
                dt_ezsigndocument_duedate = '2020-12-31 23:59:59',
                s_ezsigndocument_name = 'Contract #123',
                s_ezsigndocument_externalid = '{"ID": 1234, "TAGS": ["tag1", "tag2", "tag3"]}'
            )
        else:
            return EzsigndocumentRequestCompound(
                fki_ezsignfolder_id = 33,
                fki_language_id = 2,
                e_ezsigndocument_source = 'Base64',
                dt_ezsigndocument_duedate = '2020-12-31 23:59:59',
                s_ezsigndocument_name = 'Contract #123',
        )
        """

    def testEzsigndocumentRequestCompound(self):
        """Test EzsigndocumentRequestCompound"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
