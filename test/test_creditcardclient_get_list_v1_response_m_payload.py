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

from eZmaxApi.models.creditcardclient_get_list_v1_response_m_payload import CreditcardclientGetListV1ResponseMPayload

class TestCreditcardclientGetListV1ResponseMPayload(unittest.TestCase):
    """CreditcardclientGetListV1ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreditcardclientGetListV1ResponseMPayload:
        """Test CreditcardclientGetListV1ResponseMPayload
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreditcardclientGetListV1ResponseMPayload`
        """
        model = CreditcardclientGetListV1ResponseMPayload()
        if include_optional:
            return CreditcardclientGetListV1ResponseMPayload(
                i_row_returned = 100,
                i_row_filtered = 533,
                a_obj_creditcardclient = [
                    eZmaxApi.models.creditcardclient_list_element.creditcardclient-ListElement(
                        pki_creditcardclient_id = 114, 
                        fki_creditcarddetail_id = 53, 
                        fki_creditcardtype_id = 2, 
                        b_creditcardclientrelation_isdefault = True, 
                        s_creditcardclient_description = 'Visa', 
                        b_creditcardclient_allowedcompanypayment = True, 
                        b_creditcardclient_allowedtranquillit = True, 
                        i_creditcarddetail_expirationmonth = 10, 
                        i_creditcarddetail_expirationyear = 2024, 
                        i_creditcarddetail_lastdigits = 4242, )
                    ]
            )
        else:
            return CreditcardclientGetListV1ResponseMPayload(
                i_row_returned = 100,
                i_row_filtered = 533,
                a_obj_creditcardclient = [
                    eZmaxApi.models.creditcardclient_list_element.creditcardclient-ListElement(
                        pki_creditcardclient_id = 114, 
                        fki_creditcarddetail_id = 53, 
                        fki_creditcardtype_id = 2, 
                        b_creditcardclientrelation_isdefault = True, 
                        s_creditcardclient_description = 'Visa', 
                        b_creditcardclient_allowedcompanypayment = True, 
                        b_creditcardclient_allowedtranquillit = True, 
                        i_creditcarddetail_expirationmonth = 10, 
                        i_creditcarddetail_expirationyear = 2024, 
                        i_creditcarddetail_lastdigits = 4242, )
                    ],
        )
        """

    def testCreditcardclientGetListV1ResponseMPayload(self):
        """Test CreditcardclientGetListV1ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
