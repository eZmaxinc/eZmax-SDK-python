"""
    eZmax API Definition (Full)

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.1.11
    Contact: support-api@ezmax.ca
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import eZmaxApi
from eZmaxApi.model.field_pki_agent_id import FieldPkiAgentID
from eZmaxApi.model.field_pki_broker_id import FieldPkiBrokerID
from eZmaxApi.model.field_pki_customer_id import FieldPkiCustomerID
from eZmaxApi.model.field_pki_employee_id import FieldPkiEmployeeID
globals()['FieldPkiAgentID'] = FieldPkiAgentID
globals()['FieldPkiBrokerID'] = FieldPkiBrokerID
globals()['FieldPkiCustomerID'] = FieldPkiCustomerID
globals()['FieldPkiEmployeeID'] = FieldPkiEmployeeID
from eZmaxApi.model.department_get_members_v1_response_m_payload import DepartmentGetMembersV1ResponseMPayload


class TestDepartmentGetMembersV1ResponseMPayload(unittest.TestCase):
    """DepartmentGetMembersV1ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDepartmentGetMembersV1ResponseMPayload(self):
        """Test DepartmentGetMembersV1ResponseMPayload"""
        # FIXME: construct object with mandatory attributes with example values
        # model = DepartmentGetMembersV1ResponseMPayload()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
