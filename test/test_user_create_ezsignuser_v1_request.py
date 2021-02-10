"""
    eZmax API Definition

    This API expose all the functionnalities for the eZmax and eZsign application.  We provide SDKs for customers. They are generated using OpenAPI codegen, we encourage customers to use them as we also provide samples for them.  You can choose to build your own implementation manually or can use any compatible OpenAPI 3.0 generator like Swagger Codegen, OpenAPI codegen or any commercial generators.  If you need helping understanding how to use this API, don't waste too much time looking for it. Contact support-api@ezmax.ca, we're here to help. We are developpers so we know programmers don't like bad documentation. If you don't find what you need in the documentation, let us know, we'll improve it and put you rapidly up on track.  # noqa: E501

    The version of the OpenAPI document: 1.0.29
    Contact: support-api@ezmax.ca
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import eZmaxinc/eZmax-SDK-python
from eZmaxinc/eZmax-SDK-python.model.field_pki_language_id import FieldPkiLanguageID
globals()['FieldPkiLanguageID'] = FieldPkiLanguageID
from eZmaxinc/eZmax-SDK-python.model.user_create_ezsignuser_v1_request import UserCreateEzsignuserV1Request


class TestUserCreateEzsignuserV1Request(unittest.TestCase):
    """UserCreateEzsignuserV1Request unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testUserCreateEzsignuserV1Request(self):
        """Test UserCreateEzsignuserV1Request"""
        # FIXME: construct object with mandatory attributes with example values
        # model = UserCreateEzsignuserV1Request()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
