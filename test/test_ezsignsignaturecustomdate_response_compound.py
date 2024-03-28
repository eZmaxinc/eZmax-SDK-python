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

from eZmaxApi.models.ezsignsignaturecustomdate_response_compound import EzsignsignaturecustomdateResponseCompound

class TestEzsignsignaturecustomdateResponseCompound(unittest.TestCase):
    """EzsignsignaturecustomdateResponseCompound unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsignsignaturecustomdateResponseCompound:
        """Test EzsignsignaturecustomdateResponseCompound
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsignsignaturecustomdateResponseCompound`
        """
        model = EzsignsignaturecustomdateResponseCompound()
        if include_optional:
            return EzsignsignaturecustomdateResponseCompound(
                pki_ezsignsignaturecustomdate_id = 27,
                i_ezsignsignaturecustomdate_x = 200,
                i_ezsignsignaturecustomdate_y = 300,
                i_ezsignsignaturecustomdate_offsetx = 200,
                i_ezsignsignaturecustomdate_offsety = 300,
                s_ezsignsignaturecustomdate_format = 'Signature date: {YYYY}/{MM}/{DD} {hh}:{mm}{ss} {Z}'
            )
        else:
            return EzsignsignaturecustomdateResponseCompound(
                pki_ezsignsignaturecustomdate_id = 27,
                s_ezsignsignaturecustomdate_format = 'Signature date: {YYYY}/{MM}/{DD} {hh}:{mm}{ss} {Z}',
        )
        """

    def testEzsignsignaturecustomdateResponseCompound(self):
        """Test EzsignsignaturecustomdateResponseCompound"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
