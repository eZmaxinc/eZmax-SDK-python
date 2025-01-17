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

from eZmaxApi.models.ezsignsignature_sign_v1_response import EzsignsignatureSignV1Response

class TestEzsignsignatureSignV1Response(unittest.TestCase):
    """EzsignsignatureSignV1Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsignsignatureSignV1Response:
        """Test EzsignsignatureSignV1Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsignsignatureSignV1Response`
        """
        model = EzsignsignatureSignV1Response()
        if include_optional:
            return EzsignsignatureSignV1Response(
                m_payload = eZmaxApi.models.ezsignsignature_sign_v1_response_m_payload.ezsignsignature-sign-v1-Response-mPayload(
                    dt_ezsignsignature_date_in_folder_timezone = '2020-12-31 23:59:59', 
                    obj_timezone = eZmaxApi.models.custom_timezone_with_code_response.Custom-TimezoneWithCode-Response(
                        s_timezone_name = '', 
                        s_code = 'EST', ), )
            )
        else:
            return EzsignsignatureSignV1Response(
                m_payload = eZmaxApi.models.ezsignsignature_sign_v1_response_m_payload.ezsignsignature-sign-v1-Response-mPayload(
                    dt_ezsignsignature_date_in_folder_timezone = '2020-12-31 23:59:59', 
                    obj_timezone = eZmaxApi.models.custom_timezone_with_code_response.Custom-TimezoneWithCode-Response(
                        s_timezone_name = '', 
                        s_code = 'EST', ), ),
        )
        """

    def testEzsignsignatureSignV1Response(self):
        """Test EzsignsignatureSignV1Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
