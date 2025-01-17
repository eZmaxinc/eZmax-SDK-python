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

from eZmaxApi.models.ezsignfolder_send_v3_response import EzsignfolderSendV3Response

class TestEzsignfolderSendV3Response(unittest.TestCase):
    """EzsignfolderSendV3Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsignfolderSendV3Response:
        """Test EzsignfolderSendV3Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsignfolderSendV3Response`
        """
        model = EzsignfolderSendV3Response()
        if include_optional:
            return EzsignfolderSendV3Response(
            )
        else:
            return EzsignfolderSendV3Response(
        )
        """

    def testEzsignfolderSendV3Response(self):
        """Test EzsignfolderSendV3Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
