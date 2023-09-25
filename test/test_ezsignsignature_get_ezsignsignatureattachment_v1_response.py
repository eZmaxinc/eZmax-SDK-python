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
import datetime

from eZmaxApi.models.ezsignsignature_get_ezsignsignatureattachment_v1_response import EzsignsignatureGetEzsignsignatureattachmentV1Response  # noqa: E501

class TestEzsignsignatureGetEzsignsignatureattachmentV1Response(unittest.TestCase):
    """EzsignsignatureGetEzsignsignatureattachmentV1Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsignsignatureGetEzsignsignatureattachmentV1Response:
        """Test EzsignsignatureGetEzsignsignatureattachmentV1Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsignsignatureGetEzsignsignatureattachmentV1Response`
        """
        model = EzsignsignatureGetEzsignsignatureattachmentV1Response()  # noqa: E501
        if include_optional:
            return EzsignsignatureGetEzsignsignatureattachmentV1Response(
                obj_debug_payload = eZmaxApi.models.common_response_obj_debug_payload.Common-Response-objDebugPayload(
                    i_version_min = 1, 
                    i_version_max = 2, 
                    a_required_permission = [
                        117
                        ], 
                    b_version_deprecated = False, ),
                obj_debug = {"sMemoryUsage":"11,923MB","sRunTime":"0.6084s","iSQLSelects":3,"iSQLQueries":6,"a_objSQLQuery":[{"sQuery":"SELECT * FROM table","fDuration":1.0E-4},{"sQuery":"SELECT * FROM table","fDuration":1.0E-4}]},
                m_payload = eZmaxApi.models.ezsignsignature_get_ezsignsignatureattachment_v1_response_m_payload.ezsignsignature-getEzsignsignatureattachment-v1-Response-mPayload(
                    a_obj_ezsignsignatureattachment = [
                        eZmaxApi.models.ezsignsignatureattachment_response.ezsignsignatureattachment-Response(
                            pki_ezsignsignatureattachment_id = 177, 
                            fki_ezsignsignature_id = 49, 
                            bin_ezsignsignatureattachment_md5 = '098f6bcd4621d373cade4e832627b4f6', 
                            s_ezsignsignatureattachment_name = 'document.pdf', 
                            s_download_url = 'http://www.example.com/document.pdf', )
                        ], )
            )
        else:
            return EzsignsignatureGetEzsignsignatureattachmentV1Response(
                obj_debug_payload = eZmaxApi.models.common_response_obj_debug_payload.Common-Response-objDebugPayload(
                    i_version_min = 1, 
                    i_version_max = 2, 
                    a_required_permission = [
                        117
                        ], 
                    b_version_deprecated = False, ),
                m_payload = eZmaxApi.models.ezsignsignature_get_ezsignsignatureattachment_v1_response_m_payload.ezsignsignature-getEzsignsignatureattachment-v1-Response-mPayload(
                    a_obj_ezsignsignatureattachment = [
                        eZmaxApi.models.ezsignsignatureattachment_response.ezsignsignatureattachment-Response(
                            pki_ezsignsignatureattachment_id = 177, 
                            fki_ezsignsignature_id = 49, 
                            bin_ezsignsignatureattachment_md5 = '098f6bcd4621d373cade4e832627b4f6', 
                            s_ezsignsignatureattachment_name = 'document.pdf', 
                            s_download_url = 'http://www.example.com/document.pdf', )
                        ], ),
        )
        """

    def testEzsignsignatureGetEzsignsignatureattachmentV1Response(self):
        """Test EzsignsignatureGetEzsignsignatureattachmentV1Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
