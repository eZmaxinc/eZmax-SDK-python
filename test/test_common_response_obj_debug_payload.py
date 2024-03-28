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

from eZmaxApi.models.common_response_obj_debug_payload import CommonResponseObjDebugPayload

class TestCommonResponseObjDebugPayload(unittest.TestCase):
    """CommonResponseObjDebugPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CommonResponseObjDebugPayload:
        """Test CommonResponseObjDebugPayload
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CommonResponseObjDebugPayload`
        """
        model = CommonResponseObjDebugPayload()
        if include_optional:
            return CommonResponseObjDebugPayload(
                i_version_min = 1,
                i_version_max = 2,
                a_required_permission = [
                    117
                    ],
                b_version_deprecated = False
            )
        else:
            return CommonResponseObjDebugPayload(
                i_version_min = 1,
                i_version_max = 2,
                a_required_permission = [
                    117
                    ],
                b_version_deprecated = False,
        )
        """

    def testCommonResponseObjDebugPayload(self):
        """Test CommonResponseObjDebugPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
