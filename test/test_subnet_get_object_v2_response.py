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

from eZmaxApi.models.subnet_get_object_v2_response import SubnetGetObjectV2Response  # noqa: E501

class TestSubnetGetObjectV2Response(unittest.TestCase):
    """SubnetGetObjectV2Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SubnetGetObjectV2Response:
        """Test SubnetGetObjectV2Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SubnetGetObjectV2Response`
        """
        model = SubnetGetObjectV2Response()  # noqa: E501
        if include_optional:
            return SubnetGetObjectV2Response(
                obj_debug_payload = eZmaxApi.models.common_response_obj_debug_payload.Common-Response-objDebugPayload(
                    i_version_min = 1, 
                    i_version_max = 2, 
                    a_required_permission = [
                        117
                        ], 
                    b_version_deprecated = False, ),
                obj_debug = {"sMemoryUsage":"11,923MB","sRunTime":"0.6084s","iSQLSelects":3,"iSQLQueries":6,"a_objSQLQuery":[{"sQuery":"SELECT * FROM table","fDuration":1.0E-4},{"sQuery":"SELECT * FROM table","fDuration":1.0E-4}]},
                m_payload = eZmaxApi.models.subnet_get_object_v2_response_m_payload.subnet-getObject-v2-Response-mPayload(
                    obj_subnet = eZmaxApi.models.subnet_response_compound.subnet-ResponseCompound(), )
            )
        else:
            return SubnetGetObjectV2Response(
                obj_debug_payload = eZmaxApi.models.common_response_obj_debug_payload.Common-Response-objDebugPayload(
                    i_version_min = 1, 
                    i_version_max = 2, 
                    a_required_permission = [
                        117
                        ], 
                    b_version_deprecated = False, ),
                m_payload = eZmaxApi.models.subnet_get_object_v2_response_m_payload.subnet-getObject-v2-Response-mPayload(
                    obj_subnet = eZmaxApi.models.subnet_response_compound.subnet-ResponseCompound(), ),
        )
        """

    def testSubnetGetObjectV2Response(self):
        """Test SubnetGetObjectV2Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
