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

from eZmaxApi.models.ezsigntemplate_request import EzsigntemplateRequest

class TestEzsigntemplateRequest(unittest.TestCase):
    """EzsigntemplateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsigntemplateRequest:
        """Test EzsigntemplateRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsigntemplateRequest`
        """
        model = EzsigntemplateRequest()
        if include_optional:
            return EzsigntemplateRequest(
                pki_ezsigntemplate_id = 36,
                fki_ezsignfoldertype_id = 5,
                fki_language_id = 2,
                s_ezsigntemplate_description = 'Standard Contract',
                s_ezsigntemplate_filenamepattern = 'Contract',
                b_ezsigntemplate_adminonly = True
            )
        else:
            return EzsigntemplateRequest(
                fki_ezsignfoldertype_id = 5,
                fki_language_id = 2,
                s_ezsigntemplate_description = 'Standard Contract',
                b_ezsigntemplate_adminonly = True,
        )
        """

    def testEzsigntemplateRequest(self):
        """Test EzsigntemplateRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
