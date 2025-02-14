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

from eZmaxApi.models.ezsigntemplateglobal_response import EzsigntemplateglobalResponse

class TestEzsigntemplateglobalResponse(unittest.TestCase):
    """EzsigntemplateglobalResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsigntemplateglobalResponse:
        """Test EzsigntemplateglobalResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsigntemplateglobalResponse`
        """
        model = EzsigntemplateglobalResponse()
        if include_optional:
            return EzsigntemplateglobalResponse(
                pki_ezsigntemplateglobal_id = 36,
                fki_ezsigntemplateglobaldocument_id = 133,
                fki_module_id = 40,
                s_module_name_x = 'Purchase',
                fki_language_id = 2,
                s_language_name_x = 'English',
                e_ezsigntemplateglobal_module = 'All',
                e_ezsigntemplateglobal_supplier = 'Centris',
                s_ezsigntemplateglobal_code = 'DR-FR',
                s_ezsigntemplateglobal_description = 'Standard Contract'
            )
        else:
            return EzsigntemplateglobalResponse(
                pki_ezsigntemplateglobal_id = 36,
                fki_ezsigntemplateglobaldocument_id = 133,
                fki_module_id = 40,
                fki_language_id = 2,
                s_language_name_x = 'English',
                e_ezsigntemplateglobal_module = 'All',
                e_ezsigntemplateglobal_supplier = 'Centris',
                s_ezsigntemplateglobal_code = 'DR-FR',
                s_ezsigntemplateglobal_description = 'Standard Contract',
        )
        """

    def testEzsigntemplateglobalResponse(self):
        """Test EzsigntemplateglobalResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
