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

from eZmaxApi.models.ezsignfolder_send_v1_request import EzsignfolderSendV1Request

class TestEzsignfolderSendV1Request(unittest.TestCase):
    """EzsignfolderSendV1Request unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsignfolderSendV1Request:
        """Test EzsignfolderSendV1Request
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsignfolderSendV1Request`
        """
        model = EzsignfolderSendV1Request()
        if include_optional:
            return EzsignfolderSendV1Request(
                t_extra_message = 'Hi John,

This is the document I need you to review.

Could you sign it before Monday please.

Best Regards.

Mary'
            )
        else:
            return EzsignfolderSendV1Request(
                t_extra_message = 'Hi John,

This is the document I need you to review.

Could you sign it before Monday please.

Best Regards.

Mary',
        )
        """

    def testEzsignfolderSendV1Request(self):
        """Test EzsignfolderSendV1Request"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
