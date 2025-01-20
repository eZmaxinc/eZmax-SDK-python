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

from eZmaxApi.models.ezsignsignature_sign_v1_request import EzsignsignatureSignV1Request

class TestEzsignsignatureSignV1Request(unittest.TestCase):
    """EzsignsignatureSignV1Request unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsignsignatureSignV1Request:
        """Test EzsignsignatureSignV1Request
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsignsignatureSignV1Request`
        """
        model = EzsignsignatureSignV1Request()
        if include_optional:
            return EzsignsignatureSignV1Request(
                fki_ezsignsigningreason_id = 194,
                fki_font_id = 1,
                s_value = '',
                e_attachments_confirmation_decision = 'Accepted',
                s_attachments_refusal_reason = '',
                s_svg = '{"$ref":"#/components/examples/Svg/value"}',
                a_obj_file = [
                    eZmaxApi.models.common_file.Common-File(
                        s_file_name = 'example.pdf', 
                        s_file_url = '', 
                        s_file_base64 = '[B@754777cd', 
                        e_file_source = 'Base64', )
                    ],
                b_is_automatic = True
            )
        else:
            return EzsignsignatureSignV1Request(
                b_is_automatic = True,
        )
        """

    def testEzsignsignatureSignV1Request(self):
        """Test EzsignsignatureSignV1Request"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
