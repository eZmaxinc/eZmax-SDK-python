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

from eZmaxApi.models.textstylestatic_response_compound import TextstylestaticResponseCompound  # noqa: E501

class TestTextstylestaticResponseCompound(unittest.TestCase):
    """TextstylestaticResponseCompound unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TextstylestaticResponseCompound:
        """Test TextstylestaticResponseCompound
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TextstylestaticResponseCompound`
        """
        model = TextstylestaticResponseCompound()  # noqa: E501
        if include_optional:
            return TextstylestaticResponseCompound(
                pki_textstylestatic_id = 216,
                fki_font_id = 1,
                b_textstylestatic_bold = True,
                b_textstylestatic_underline = True,
                b_textstylestatic_italic = True,
                b_textstylestatic_strikethrough = True,
                i_textstylestatic_fontcolor = 3752795,
                i_textstylestatic_size = 12
            )
        else:
            return TextstylestaticResponseCompound(
                fki_font_id = 1,
                b_textstylestatic_bold = True,
                b_textstylestatic_underline = True,
                b_textstylestatic_italic = True,
                b_textstylestatic_strikethrough = True,
                i_textstylestatic_fontcolor = 3752795,
                i_textstylestatic_size = 12,
        )
        """

    def testTextstylestaticResponseCompound(self):
        """Test TextstylestaticResponseCompound"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()