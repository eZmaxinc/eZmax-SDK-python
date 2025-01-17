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

from eZmaxApi.models.common_response_error_creditcard_validation import CommonResponseErrorCreditcardValidation

class TestCommonResponseErrorCreditcardValidation(unittest.TestCase):
    """CommonResponseErrorCreditcardValidation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CommonResponseErrorCreditcardValidation:
        """Test CommonResponseErrorCreditcardValidation
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CommonResponseErrorCreditcardValidation`
        """
        model = CommonResponseErrorCreditcardValidation()
        if include_optional:
            return CommonResponseErrorCreditcardValidation(
                obj_creditcardtransactionresponse = eZmaxApi.models.custom_creditcardtransactionresponse_response.Custom-Creditcardtransactionresponse-Response(
                    s_creditcardtransaction_is_ocode = '01', 
                    s_creditcardtransaction_responsecode = '027', 
                    s_creditcardtransaction_responseterminalmessage = 'APPROVED', 
                    e_creditcardtransaction_avsresult = 'Match', 
                    e_creditcardtransaction_cvdresult = 'Match', )
            )
        else:
            return CommonResponseErrorCreditcardValidation(
        )
        """

    def testCommonResponseErrorCreditcardValidation(self):
        """Test CommonResponseErrorCreditcardValidation"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
