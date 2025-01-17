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

from eZmaxApi.models.user_get_colleagues_v2_response import UserGetColleaguesV2Response

class TestUserGetColleaguesV2Response(unittest.TestCase):
    """UserGetColleaguesV2Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserGetColleaguesV2Response:
        """Test UserGetColleaguesV2Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserGetColleaguesV2Response`
        """
        model = UserGetColleaguesV2Response()
        if include_optional:
            return UserGetColleaguesV2Response(
                m_payload = eZmaxApi.models.user_get_colleagues_v2_response_m_payload.user-getColleagues-v2-Response-mPayload(
                    a_obj_colleague = [
                        eZmaxApi.models.colleague_response_compound_v2.colleague-ResponseCompoundV2()
                        ], 
                    a_obj_colleague_clonable = [
                        eZmaxApi.models.colleague_response_compound_v2.colleague-ResponseCompoundV2()
                        ], )
            )
        else:
            return UserGetColleaguesV2Response(
                m_payload = eZmaxApi.models.user_get_colleagues_v2_response_m_payload.user-getColleagues-v2-Response-mPayload(
                    a_obj_colleague = [
                        eZmaxApi.models.colleague_response_compound_v2.colleague-ResponseCompoundV2()
                        ], 
                    a_obj_colleague_clonable = [
                        eZmaxApi.models.colleague_response_compound_v2.colleague-ResponseCompoundV2()
                        ], ),
        )
        """

    def testUserGetColleaguesV2Response(self):
        """Test UserGetColleaguesV2Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
