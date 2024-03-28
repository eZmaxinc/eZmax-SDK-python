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

from eZmaxApi.models.period_autocomplete_element_response import PeriodAutocompleteElementResponse

class TestPeriodAutocompleteElementResponse(unittest.TestCase):
    """PeriodAutocompleteElementResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PeriodAutocompleteElementResponse:
        """Test PeriodAutocompleteElementResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PeriodAutocompleteElementResponse`
        """
        model = PeriodAutocompleteElementResponse()
        if include_optional:
            return PeriodAutocompleteElementResponse(
                s_period_yyyymm = '2202-12',
                pki_period_id = 21,
                b_period_isactive = True
            )
        else:
            return PeriodAutocompleteElementResponse(
                s_period_yyyymm = '2202-12',
                pki_period_id = 21,
                b_period_isactive = True,
        )
        """

    def testPeriodAutocompleteElementResponse(self):
        """Test PeriodAutocompleteElementResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
