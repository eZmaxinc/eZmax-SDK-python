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

from eZmaxApi.models.ezsignfolder_reorder_v2_response import EzsignfolderReorderV2Response

class TestEzsignfolderReorderV2Response(unittest.TestCase):
    """EzsignfolderReorderV2Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsignfolderReorderV2Response:
        """Test EzsignfolderReorderV2Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsignfolderReorderV2Response`
        """
        model = EzsignfolderReorderV2Response()
        if include_optional:
            return EzsignfolderReorderV2Response(
            )
        else:
            return EzsignfolderReorderV2Response(
        )
        """

    def testEzsignfolderReorderV2Response(self):
        """Test EzsignfolderReorderV2Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
