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

from eZmaxApi.models.phone_request_compound import PhoneRequestCompound

class TestPhoneRequestCompound(unittest.TestCase):
    """PhoneRequestCompound unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PhoneRequestCompound:
        """Test PhoneRequestCompound
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PhoneRequestCompound`
        """
        model = PhoneRequestCompound()
        if include_optional:
            return PhoneRequestCompound(
                pki_phone_id = 1,
                fki_phonetype_id = 1,
                e_phone_type = 'Local',
                s_phone_region = '514',
                s_phone_exchange = '990',
                s_phone_number = '1516',
                s_phone_international = '15149901516',
                s_phone_extension = '123',
                s_phone_e164 = '+15149901516'
            )
        else:
            return PhoneRequestCompound(
                fki_phonetype_id = 1,
        )
        """

    def testPhoneRequestCompound(self):
        """Test PhoneRequestCompound"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
