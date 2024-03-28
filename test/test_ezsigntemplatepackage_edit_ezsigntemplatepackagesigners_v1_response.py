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

from eZmaxApi.models.ezsigntemplatepackage_edit_ezsigntemplatepackagesigners_v1_response import EzsigntemplatepackageEditEzsigntemplatepackagesignersV1Response

class TestEzsigntemplatepackageEditEzsigntemplatepackagesignersV1Response(unittest.TestCase):
    """EzsigntemplatepackageEditEzsigntemplatepackagesignersV1Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsigntemplatepackageEditEzsigntemplatepackagesignersV1Response:
        """Test EzsigntemplatepackageEditEzsigntemplatepackagesignersV1Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsigntemplatepackageEditEzsigntemplatepackagesignersV1Response`
        """
        model = EzsigntemplatepackageEditEzsigntemplatepackagesignersV1Response()
        if include_optional:
            return EzsigntemplatepackageEditEzsigntemplatepackagesignersV1Response(
                obj_debug_payload = eZmaxApi.models.common_response_obj_debug_payload.Common-Response-objDebugPayload(
                    i_version_min = 1, 
                    i_version_max = 2, 
                    a_required_permission = [
                        117
                        ], 
                    b_version_deprecated = False, ),
                obj_debug = {"sMemoryUsage":"11,923MB","sRunTime":"0.6084s","iSQLSelects":3,"iSQLQueries":6,"a_objSQLQuery":[{"sQuery":"SELECT * FROM table","fDuration":1.0E-4},{"sQuery":"SELECT * FROM table","fDuration":1.0E-4}]},
                m_payload = eZmaxApi.models.ezsigntemplatepackage_edit_ezsigntemplatepackagesigners_v1_response_m_payload.ezsigntemplatepackage-editEzsigntemplatepackagesigners-v1-Response-mPayload(
                    a_pki_ezsigntemplatepackagesigner_id = [
                        174
                        ], )
            )
        else:
            return EzsigntemplatepackageEditEzsigntemplatepackagesignersV1Response(
                obj_debug_payload = eZmaxApi.models.common_response_obj_debug_payload.Common-Response-objDebugPayload(
                    i_version_min = 1, 
                    i_version_max = 2, 
                    a_required_permission = [
                        117
                        ], 
                    b_version_deprecated = False, ),
                m_payload = eZmaxApi.models.ezsigntemplatepackage_edit_ezsigntemplatepackagesigners_v1_response_m_payload.ezsigntemplatepackage-editEzsigntemplatepackagesigners-v1-Response-mPayload(
                    a_pki_ezsigntemplatepackagesigner_id = [
                        174
                        ], ),
        )
        """

    def testEzsigntemplatepackageEditEzsigntemplatepackagesignersV1Response(self):
        """Test EzsigntemplatepackageEditEzsigntemplatepackagesignersV1Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
