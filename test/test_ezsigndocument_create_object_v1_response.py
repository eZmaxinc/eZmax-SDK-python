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

from eZmaxApi.models.ezsigndocument_create_object_v1_response import EzsigndocumentCreateObjectV1Response

class TestEzsigndocumentCreateObjectV1Response(unittest.TestCase):
    """EzsigndocumentCreateObjectV1Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsigndocumentCreateObjectV1Response:
        """Test EzsigndocumentCreateObjectV1Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsigndocumentCreateObjectV1Response`
        """
        model = EzsigndocumentCreateObjectV1Response()
        if include_optional:
            return EzsigndocumentCreateObjectV1Response(
                obj_debug_payload = eZmaxApi.models.common_response_obj_debug_payload.Common-Response-objDebugPayload(
                    i_version_min = 1, 
                    i_version_max = 2, 
                    a_required_permission = [
                        117
                        ], 
                    b_version_deprecated = False, ),
                obj_debug = {"sMemoryUsage":"11,923MB","sRunTime":"0.6084s","iSQLSelects":3,"iSQLQueries":6,"a_objSQLQuery":[{"sQuery":"SELECT * FROM table","fDuration":1.0E-4},{"sQuery":"SELECT * FROM table","fDuration":1.0E-4}]},
                m_payload = eZmaxApi.models.ezsigndocument_create_object_v1_response_m_payload.ezsigndocument-createObject-v1-Response-mPayload(
                    a_pki_ezsigndocument_id = [
                        97
                        ], )
            )
        else:
            return EzsigndocumentCreateObjectV1Response(
                obj_debug_payload = eZmaxApi.models.common_response_obj_debug_payload.Common-Response-objDebugPayload(
                    i_version_min = 1, 
                    i_version_max = 2, 
                    a_required_permission = [
                        117
                        ], 
                    b_version_deprecated = False, ),
                m_payload = eZmaxApi.models.ezsigndocument_create_object_v1_response_m_payload.ezsigndocument-createObject-v1-Response-mPayload(
                    a_pki_ezsigndocument_id = [
                        97
                        ], ),
        )
        """

    def testEzsigndocumentCreateObjectV1Response(self):
        """Test EzsigndocumentCreateObjectV1Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
