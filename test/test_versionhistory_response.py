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
from eZmaxApi.model.field_e_versionhistory_type import FieldEVersionhistoryType
from eZmaxApi.model.field_e_versionhistory_usertype import FieldEVersionhistoryUsertype
from eZmaxApi.model.field_pki_module_id import FieldPkiModuleID
from eZmaxApi.model.field_pki_modulesection_id import FieldPkiModulesectionID
from eZmaxApi.model.field_pki_versionhistory_id import FieldPkiVersionhistoryID
from eZmaxApi.model.multilingual_versionhistory_detail import MultilingualVersionhistoryDetail
globals()['FieldEVersionhistoryType'] = FieldEVersionhistoryType
globals()['FieldEVersionhistoryUsertype'] = FieldEVersionhistoryUsertype
globals()['FieldPkiModuleID'] = FieldPkiModuleID
globals()['FieldPkiModulesectionID'] = FieldPkiModulesectionID
globals()['FieldPkiVersionhistoryID'] = FieldPkiVersionhistoryID
globals()['MultilingualVersionhistoryDetail'] = MultilingualVersionhistoryDetail
from eZmaxApi.model.versionhistory_response import VersionhistoryResponse


class TestVersionhistoryResponse(unittest.TestCase):
    """VersionhistoryResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testVersionhistoryResponse(self):
        """Test VersionhistoryResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = VersionhistoryResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()