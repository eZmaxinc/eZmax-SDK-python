"""
    eZmax API Definition (Full)

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.1.10
    Contact: support-api@ezmax.ca
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import eZmaxApi
from eZmaxApi.model.custom_form_data_ezsignformfieldgroup_response import CustomFormDataEzsignformfieldgroupResponse
from eZmaxApi.model.field_pki_ezsignfoldersignerassociation_id import FieldPkiEzsignfoldersignerassociationID
from eZmaxApi.model.field_pki_user_id import FieldPkiUserID
globals()['CustomFormDataEzsignformfieldgroupResponse'] = CustomFormDataEzsignformfieldgroupResponse
globals()['FieldPkiEzsignfoldersignerassociationID'] = FieldPkiEzsignfoldersignerassociationID
globals()['FieldPkiUserID'] = FieldPkiUserID
from eZmaxApi.model.custom_form_data_signer_response import CustomFormDataSignerResponse


class TestCustomFormDataSignerResponse(unittest.TestCase):
    """CustomFormDataSignerResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCustomFormDataSignerResponse(self):
        """Test CustomFormDataSignerResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = CustomFormDataSignerResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
