"""
    eZmax API Definition (Full)

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.1.12
    Contact: support-api@ezmax.ca
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import eZmaxApi
from eZmaxApi.model.custom_form_data_document_response import CustomFormDataDocumentResponse
from eZmaxApi.model.field_pki_ezsignfolder_id import FieldPkiEzsignfolderID
globals()['CustomFormDataDocumentResponse'] = CustomFormDataDocumentResponse
globals()['FieldPkiEzsignfolderID'] = FieldPkiEzsignfolderID
from eZmaxApi.model.custom_forms_data_folder_response import CustomFormsDataFolderResponse


class TestCustomFormsDataFolderResponse(unittest.TestCase):
    """CustomFormsDataFolderResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCustomFormsDataFolderResponse(self):
        """Test CustomFormsDataFolderResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = CustomFormsDataFolderResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
