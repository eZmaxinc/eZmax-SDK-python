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

from eZmaxApi.models.ezsigntemplateformfieldgroup_get_object_v2_response import EzsigntemplateformfieldgroupGetObjectV2Response

class TestEzsigntemplateformfieldgroupGetObjectV2Response(unittest.TestCase):
    """EzsigntemplateformfieldgroupGetObjectV2Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsigntemplateformfieldgroupGetObjectV2Response:
        """Test EzsigntemplateformfieldgroupGetObjectV2Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsigntemplateformfieldgroupGetObjectV2Response`
        """
        model = EzsigntemplateformfieldgroupGetObjectV2Response()
        if include_optional:
            return EzsigntemplateformfieldgroupGetObjectV2Response(
                obj_debug_payload = eZmaxApi.models.common_response_obj_debug_payload.Common-Response-objDebugPayload(
                    i_version_min = 1, 
                    i_version_max = 2, 
                    a_required_permission = [
                        117
                        ], 
                    b_version_deprecated = False, ),
                obj_debug = {"sMemoryUsage":"11,923MB","sRunTime":"0.6084s","iSQLSelects":3,"iSQLQueries":6,"a_objSQLQuery":[{"sQuery":"SELECT * FROM table","fDuration":1.0E-4},{"sQuery":"SELECT * FROM table","fDuration":1.0E-4}]},
                m_payload = eZmaxApi.models.ezsigntemplateformfieldgroup_get_object_v2_response_m_payload.ezsigntemplateformfieldgroup-getObject-v2-Response-mPayload(
                    obj_ezsigntemplateformfieldgroup = eZmaxApi.models.ezsigntemplateformfieldgroup_response_compound.ezsigntemplateformfieldgroup-ResponseCompound(), )
            )
        else:
            return EzsigntemplateformfieldgroupGetObjectV2Response(
                obj_debug_payload = eZmaxApi.models.common_response_obj_debug_payload.Common-Response-objDebugPayload(
                    i_version_min = 1, 
                    i_version_max = 2, 
                    a_required_permission = [
                        117
                        ], 
                    b_version_deprecated = False, ),
                m_payload = eZmaxApi.models.ezsigntemplateformfieldgroup_get_object_v2_response_m_payload.ezsigntemplateformfieldgroup-getObject-v2-Response-mPayload(
                    obj_ezsigntemplateformfieldgroup = eZmaxApi.models.ezsigntemplateformfieldgroup_response_compound.ezsigntemplateformfieldgroup-ResponseCompound(), ),
        )
        """

    def testEzsigntemplateformfieldgroupGetObjectV2Response(self):
        """Test EzsigntemplateformfieldgroupGetObjectV2Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
