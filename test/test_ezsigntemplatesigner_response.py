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

from eZmaxApi.models.ezsigntemplatesigner_response import EzsigntemplatesignerResponse

class TestEzsigntemplatesignerResponse(unittest.TestCase):
    """EzsigntemplatesignerResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsigntemplatesignerResponse:
        """Test EzsigntemplatesignerResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsigntemplatesignerResponse`
        """
        model = EzsigntemplatesignerResponse()
        if include_optional:
            return EzsigntemplatesignerResponse(
                pki_ezsigntemplatesigner_id = 9,
                fki_ezsigntemplate_id = 36,
                s_ezsigntemplatesigner_description = 'Customer'
            )
        else:
            return EzsigntemplatesignerResponse(
                pki_ezsigntemplatesigner_id = 9,
                fki_ezsigntemplate_id = 36,
                s_ezsigntemplatesigner_description = 'Customer',
        )
        """

    def testEzsigntemplatesignerResponse(self):
        """Test EzsigntemplatesignerResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
