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

from eZmaxApi.models.ezsigntemplatesignaturecustomdate_request import EzsigntemplatesignaturecustomdateRequest

class TestEzsigntemplatesignaturecustomdateRequest(unittest.TestCase):
    """EzsigntemplatesignaturecustomdateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsigntemplatesignaturecustomdateRequest:
        """Test EzsigntemplatesignaturecustomdateRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsigntemplatesignaturecustomdateRequest`
        """
        model = EzsigntemplatesignaturecustomdateRequest()
        if include_optional:
            return EzsigntemplatesignaturecustomdateRequest(
                pki_ezsigntemplatesignaturecustomdate_id = 58,
                i_ezsigntemplatesignaturecustomdate_x = 200,
                i_ezsigntemplatesignaturecustomdate_y = 300,
                i_ezsigntemplatesignaturecustomdate_offsetx = 200,
                i_ezsigntemplatesignaturecustomdate_offsety = 200,
                s_ezsigntemplatesignaturecustomdate_format = 'Signature date: {YYYY}/{MM}/{DD} {hh}:{mm}{ss} {Z}'
            )
        else:
            return EzsigntemplatesignaturecustomdateRequest(
                s_ezsigntemplatesignaturecustomdate_format = 'Signature date: {YYYY}/{MM}/{DD} {hh}:{mm}{ss} {Z}',
        )
        """

    def testEzsigntemplatesignaturecustomdateRequest(self):
        """Test EzsigntemplatesignaturecustomdateRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
