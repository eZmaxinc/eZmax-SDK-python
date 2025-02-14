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

from eZmaxApi.models.signature_response_compound import SignatureResponseCompound

class TestSignatureResponseCompound(unittest.TestCase):
    """SignatureResponseCompound unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SignatureResponseCompound:
        """Test SignatureResponseCompound
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SignatureResponseCompound`
        """
        model = SignatureResponseCompound()
        if include_optional:
            return SignatureResponseCompound(
                pki_signature_id = 12,
                fki_font_id = 1,
                s_signature_url = 'https://www.example.com/signature.svg',
                s_signature_urlinitials = 'https://www.example.com/signature.svg'
            )
        else:
            return SignatureResponseCompound(
                pki_signature_id = 12,
        )
        """

    def testSignatureResponseCompound(self):
        """Test SignatureResponseCompound"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
