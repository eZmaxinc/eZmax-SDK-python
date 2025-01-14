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

from eZmaxApi.models.ezsigndiscussion_get_object_v2_response_m_payload import EzsigndiscussionGetObjectV2ResponseMPayload

class TestEzsigndiscussionGetObjectV2ResponseMPayload(unittest.TestCase):
    """EzsigndiscussionGetObjectV2ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsigndiscussionGetObjectV2ResponseMPayload:
        """Test EzsigndiscussionGetObjectV2ResponseMPayload
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsigndiscussionGetObjectV2ResponseMPayload`
        """
        model = EzsigndiscussionGetObjectV2ResponseMPayload()
        if include_optional:
            return EzsigndiscussionGetObjectV2ResponseMPayload(
                obj_ezsigndiscussion = eZmaxApi.models.ezsigndiscussion_response_compound.ezsigndiscussion-ResponseCompound()
            )
        else:
            return EzsigndiscussionGetObjectV2ResponseMPayload(
                obj_ezsigndiscussion = eZmaxApi.models.ezsigndiscussion_response_compound.ezsigndiscussion-ResponseCompound(),
        )
        """

    def testEzsigndiscussionGetObjectV2ResponseMPayload(self):
        """Test EzsigndiscussionGetObjectV2ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
