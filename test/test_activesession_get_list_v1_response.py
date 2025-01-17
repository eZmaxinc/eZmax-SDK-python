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

from eZmaxApi.models.activesession_get_list_v1_response import ActivesessionGetListV1Response

class TestActivesessionGetListV1Response(unittest.TestCase):
    """ActivesessionGetListV1Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ActivesessionGetListV1Response:
        """Test ActivesessionGetListV1Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ActivesessionGetListV1Response`
        """
        model = ActivesessionGetListV1Response()
        if include_optional:
            return ActivesessionGetListV1Response(
                obj_debug_payload = eZmaxApi.models.common_response_obj_debug_payload_get_list.Common-Response-objDebugPayload_getList(),
                obj_debug = {"sMemoryUsage":"11,923MB","sRunTime":"0.6084s","iSQLSelects":3,"iSQLQueries":6,"a_objSQLQuery":[{"sQuery":"SELECT * FROM table","fDuration":1.0E-4},{"sQuery":"SELECT * FROM table","fDuration":1.0E-4}]},
                m_payload = eZmaxApi.models.activesession_get_list_v1_response_m_payload.activesession-getList-v1-Response-mPayload()
            )
        else:
            return ActivesessionGetListV1Response(
                obj_debug_payload = eZmaxApi.models.common_response_obj_debug_payload_get_list.Common-Response-objDebugPayload_getList(),
                m_payload = eZmaxApi.models.activesession_get_list_v1_response_m_payload.activesession-getList-v1-Response-mPayload(),
        )
        """

    def testActivesessionGetListV1Response(self):
        """Test ActivesessionGetListV1Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
