"""
    eZmax API Definition (Full)

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.1.16
    Contact: support-api@ezmax.ca
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import eZmaxApi
from eZmaxApi.model.custom_form_data_signer_response import CustomFormDataSignerResponse
from eZmaxApi.model.field_pki_ezsigndocument_id import FieldPkiEzsigndocumentID
from eZmaxApi.model.field_pki_ezsignfolder_id import FieldPkiEzsignfolderID
globals()['CustomFormDataSignerResponse'] = CustomFormDataSignerResponse
globals()['FieldPkiEzsigndocumentID'] = FieldPkiEzsigndocumentID
globals()['FieldPkiEzsignfolderID'] = FieldPkiEzsignfolderID
from eZmaxApi.model.custom_form_data_document_response import CustomFormDataDocumentResponse


class TestCustomFormDataDocumentResponse(unittest.TestCase):
    """CustomFormDataDocumentResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCustomFormDataDocumentResponse(self):
        """Test CustomFormDataDocumentResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = CustomFormDataDocumentResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
