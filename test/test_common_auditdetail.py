"""
    eZmax API Definition (Full)

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.1.8
    Contact: support-api@ezmax.ca
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import eZmaxApi
from eZmaxApi.model.field_pki_apikey_id import FieldPkiApikeyID
from eZmaxApi.model.field_pki_user_id import FieldPkiUserID
globals()['FieldPkiApikeyID'] = FieldPkiApikeyID
globals()['FieldPkiUserID'] = FieldPkiUserID
from eZmaxApi.model.common_auditdetail import CommonAuditdetail


class TestCommonAuditdetail(unittest.TestCase):
    """CommonAuditdetail unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCommonAuditdetail(self):
        """Test CommonAuditdetail"""
        # FIXME: construct object with mandatory attributes with example values
        # model = CommonAuditdetail()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
