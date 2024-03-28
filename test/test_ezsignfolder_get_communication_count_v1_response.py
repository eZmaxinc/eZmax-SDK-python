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

from eZmaxApi.models.ezsignfolder_get_communication_count_v1_response import EzsignfolderGetCommunicationCountV1Response

class TestEzsignfolderGetCommunicationCountV1Response(unittest.TestCase):
    """EzsignfolderGetCommunicationCountV1Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsignfolderGetCommunicationCountV1Response:
        """Test EzsignfolderGetCommunicationCountV1Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsignfolderGetCommunicationCountV1Response`
        """
        model = EzsignfolderGetCommunicationCountV1Response()
        if include_optional:
            return EzsignfolderGetCommunicationCountV1Response(
                obj_debug_payload = eZmaxApi.models.common_response_obj_debug_payload.Common-Response-objDebugPayload(
                    i_version_min = 1, 
                    i_version_max = 2, 
                    a_required_permission = [
                        117
                        ], 
                    b_version_deprecated = False, ),
                obj_debug = {"sMemoryUsage":"11,923MB","sRunTime":"0.6084s","iSQLSelects":3,"iSQLQueries":6,"a_objSQLQuery":[{"sQuery":"SELECT * FROM table","fDuration":1.0E-4},{"sQuery":"SELECT * FROM table","fDuration":1.0E-4}]},
                m_payload = eZmaxApi.models.ezsignfolder_get_communication_count_v1_response_m_payload.ezsignfolder-getCommunicationCount-v1-Response-mPayload(
                    i_communication_count = 8, )
            )
        else:
            return EzsignfolderGetCommunicationCountV1Response(
                obj_debug_payload = eZmaxApi.models.common_response_obj_debug_payload.Common-Response-objDebugPayload(
                    i_version_min = 1, 
                    i_version_max = 2, 
                    a_required_permission = [
                        117
                        ], 
                    b_version_deprecated = False, ),
                m_payload = eZmaxApi.models.ezsignfolder_get_communication_count_v1_response_m_payload.ezsignfolder-getCommunicationCount-v1-Response-mPayload(
                    i_communication_count = 8, ),
        )
        """

    def testEzsignfolderGetCommunicationCountV1Response(self):
        """Test EzsignfolderGetCommunicationCountV1Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
