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

from eZmaxApi.models.ezsignfolder_reorder_v1_request import EzsignfolderReorderV1Request

class TestEzsignfolderReorderV1Request(unittest.TestCase):
    """EzsignfolderReorderV1Request unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsignfolderReorderV1Request:
        """Test EzsignfolderReorderV1Request
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsignfolderReorderV1Request`
        """
        model = EzsignfolderReorderV1Request()
        if include_optional:
            return EzsignfolderReorderV1Request(
                a_pki_ezsigndocument_id = [
                    97
                    ]
            )
        else:
            return EzsignfolderReorderV1Request(
                a_pki_ezsigndocument_id = [
                    97
                    ],
        )
        """

    def testEzsignfolderReorderV1Request(self):
        """Test EzsignfolderReorderV1Request"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
