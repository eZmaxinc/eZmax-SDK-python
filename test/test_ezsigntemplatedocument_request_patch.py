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

from eZmaxApi.models.ezsigntemplatedocument_request_patch import EzsigntemplatedocumentRequestPatch

class TestEzsigntemplatedocumentRequestPatch(unittest.TestCase):
    """EzsigntemplatedocumentRequestPatch unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsigntemplatedocumentRequestPatch:
        """Test EzsigntemplatedocumentRequestPatch
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsigntemplatedocumentRequestPatch`
        """
        model = EzsigntemplatedocumentRequestPatch()
        if include_optional:
            return EzsigntemplatedocumentRequestPatch(
                s_ezsigntemplatedocument_name = 'Standard Contract'
            )
        else:
            return EzsigntemplatedocumentRequestPatch(
        )
        """

    def testEzsigntemplatedocumentRequestPatch(self):
        """Test EzsigntemplatedocumentRequestPatch"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
