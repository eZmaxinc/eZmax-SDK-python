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

from eZmaxApi.models.phone_request_v2 import PhoneRequestV2

class TestPhoneRequestV2(unittest.TestCase):
    """PhoneRequestV2 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PhoneRequestV2:
        """Test PhoneRequestV2
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PhoneRequestV2`
        """
        model = PhoneRequestV2()
        if include_optional:
            return PhoneRequestV2(
                pki_phone_id = 1,
                fki_phonetype_id = 1,
                s_phone_extension = '123',
                s_phone_e164 = '+15149901516'
            )
        else:
            return PhoneRequestV2(
                fki_phonetype_id = 1,
        )
        """

    def testPhoneRequestV2(self):
        """Test PhoneRequestV2"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
