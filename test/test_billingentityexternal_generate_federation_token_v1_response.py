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

from eZmaxApi.models.billingentityexternal_generate_federation_token_v1_response import BillingentityexternalGenerateFederationTokenV1Response

class TestBillingentityexternalGenerateFederationTokenV1Response(unittest.TestCase):
    """BillingentityexternalGenerateFederationTokenV1Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BillingentityexternalGenerateFederationTokenV1Response:
        """Test BillingentityexternalGenerateFederationTokenV1Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BillingentityexternalGenerateFederationTokenV1Response`
        """
        model = BillingentityexternalGenerateFederationTokenV1Response()
        if include_optional:
            return BillingentityexternalGenerateFederationTokenV1Response(
                obj_debug_payload = eZmaxApi.models.common_response_obj_debug_payload.Common-Response-objDebugPayload(
                    i_version_min = 1, 
                    i_version_max = 2, 
                    a_required_permission = [
                        117
                        ], 
                    b_version_deprecated = False, 
                    dt_response_date = '2020-12-31 23:59:59', ),
                obj_debug = {"sMemoryUsage":"11,923MB","sRunTime":"0.6084s","iSQLSelects":3,"iSQLQueries":6,"a_objSQLQuery":[{"sQuery":"SELECT * FROM table","fDuration":1.0E-4},{"sQuery":"SELECT * FROM table","fDuration":1.0E-4}]},
                m_payload = eZmaxApi.models.billingentityexternal_generate_federation_token_v1_response_m_payload.billingentityexternal-generateFederationToken-v1-Response-mPayload(
                    obj_apikeyfederation = eZmaxApi.models.custom_apikeyfederation.Custom-Apikeyfederation(
                        s_apikeyfederation_key = 'jUR,rZ#UM/?R,Fp^l6$ARjbhJk C>i H\'qT\\{<?\'es#)#iK.YM{Rag2/!KB!k@5oXh.:Ts\";mGL,i&z5[P@M\"lzfB+Y,Twzfu~N^z', 
                        s_apikeyfederation_secret = 'f514d7a0008a9f6dee03e60734624d04', ), 
                    s_ezmaxcustomercode_url = 'http://www.website.com/avatar.jpg', )
            )
        else:
            return BillingentityexternalGenerateFederationTokenV1Response(
                obj_debug_payload = eZmaxApi.models.common_response_obj_debug_payload.Common-Response-objDebugPayload(
                    i_version_min = 1, 
                    i_version_max = 2, 
                    a_required_permission = [
                        117
                        ], 
                    b_version_deprecated = False, 
                    dt_response_date = '2020-12-31 23:59:59', ),
                m_payload = eZmaxApi.models.billingentityexternal_generate_federation_token_v1_response_m_payload.billingentityexternal-generateFederationToken-v1-Response-mPayload(
                    obj_apikeyfederation = eZmaxApi.models.custom_apikeyfederation.Custom-Apikeyfederation(
                        s_apikeyfederation_key = 'jUR,rZ#UM/?R,Fp^l6$ARjbhJk C>i H\'qT\\{<?\'es#)#iK.YM{Rag2/!KB!k@5oXh.:Ts\";mGL,i&z5[P@M\"lzfB+Y,Twzfu~N^z', 
                        s_apikeyfederation_secret = 'f514d7a0008a9f6dee03e60734624d04', ), 
                    s_ezmaxcustomercode_url = 'http://www.website.com/avatar.jpg', ),
        )
        """

    def testBillingentityexternalGenerateFederationTokenV1Response(self):
        """Test BillingentityexternalGenerateFederationTokenV1Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
