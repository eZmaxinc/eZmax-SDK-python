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

from eZmaxApi.models.user_create_ezsignuser_v1_response import UserCreateEzsignuserV1Response

class TestUserCreateEzsignuserV1Response(unittest.TestCase):
    """UserCreateEzsignuserV1Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserCreateEzsignuserV1Response:
        """Test UserCreateEzsignuserV1Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserCreateEzsignuserV1Response`
        """
        model = UserCreateEzsignuserV1Response()
        if include_optional:
            return UserCreateEzsignuserV1Response(
                obj_debug_payload = eZmaxApi.models.common_response_obj_debug_payload.Common-Response-objDebugPayload(
                    i_version_min = 1, 
                    i_version_max = 2, 
                    a_required_permission = [
                        117
                        ], 
                    b_version_deprecated = False, 
                    dt_response_date = '2020-12-31 23:59:59', ),
                obj_debug = {"sMemoryUsage":"11,923MB","sRunTime":"0.6084s","iSQLSelects":3,"iSQLQueries":6,"a_objSQLQuery":[{"sQuery":"SELECT * FROM table","fDuration":1.0E-4},{"sQuery":"SELECT * FROM table","fDuration":1.0E-4}]},
                m_payload = {"a_sEmailAddressSuccess":["someone@example.com","someone2@example.com"],"a_sEmailAddressFailure":["UserAlreadyExists@example.com"]}
            )
        else:
            return UserCreateEzsignuserV1Response(
                obj_debug_payload = eZmaxApi.models.common_response_obj_debug_payload.Common-Response-objDebugPayload(
                    i_version_min = 1, 
                    i_version_max = 2, 
                    a_required_permission = [
                        117
                        ], 
                    b_version_deprecated = False, 
                    dt_response_date = '2020-12-31 23:59:59', ),
                m_payload = {"a_sEmailAddressSuccess":["someone@example.com","someone2@example.com"],"a_sEmailAddressFailure":["UserAlreadyExists@example.com"]},
        )
        """

    def testUserCreateEzsignuserV1Response(self):
        """Test UserCreateEzsignuserV1Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
