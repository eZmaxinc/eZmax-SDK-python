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

from eZmaxApi.models.custom_ezsignformfielderrortest_response import CustomEzsignformfielderrortestResponse  # noqa: E501

class TestCustomEzsignformfielderrortestResponse(unittest.TestCase):
    """CustomEzsignformfielderrortestResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CustomEzsignformfielderrortestResponse:
        """Test CustomEzsignformfielderrortestResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CustomEzsignformfielderrortestResponse`
        """
        model = CustomEzsignformfielderrortestResponse()  # noqa: E501
        if include_optional:
            return CustomEzsignformfielderrortestResponse(
                s_ezsignformfielderrortest_name = 'jUR,rZ#UM/?',
                s_ezsignformfielderrortest_detail = 'jUR,rZ#UM/?R,Fp^l6$ARjbhJk C>i H'qT\\{<?'es#)#iK.YM{Rag2/!KB!k@5oXh.:Ts\";mGL,i&z5[P@M\"lzfB+Y,Twzfu~N^z\"mfqecVU{SmA{QA<Y8XX0<}J;Krm9W'g~?)DvDDLE7-'(u+-7Tfp&\\`F+7-?{%@=iEPLVY*a@A[b_6cfy~~0Gc'
            )
        else:
            return CustomEzsignformfielderrortestResponse(
                s_ezsignformfielderrortest_name = 'jUR,rZ#UM/?',
                s_ezsignformfielderrortest_detail = 'jUR,rZ#UM/?R,Fp^l6$ARjbhJk C>i H'qT\\{<?'es#)#iK.YM{Rag2/!KB!k@5oXh.:Ts\";mGL,i&z5[P@M\"lzfB+Y,Twzfu~N^z\"mfqecVU{SmA{QA<Y8XX0<}J;Krm9W'g~?)DvDDLE7-'(u+-7Tfp&\\`F+7-?{%@=iEPLVY*a@A[b_6cfy~~0Gc',
        )
        """

    def testCustomEzsignformfielderrortestResponse(self):
        """Test CustomEzsignformfielderrortestResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()