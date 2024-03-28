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

from eZmaxApi.models.systemconfiguration_get_object_v2_response_m_payload import SystemconfigurationGetObjectV2ResponseMPayload

class TestSystemconfigurationGetObjectV2ResponseMPayload(unittest.TestCase):
    """SystemconfigurationGetObjectV2ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SystemconfigurationGetObjectV2ResponseMPayload:
        """Test SystemconfigurationGetObjectV2ResponseMPayload
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SystemconfigurationGetObjectV2ResponseMPayload`
        """
        model = SystemconfigurationGetObjectV2ResponseMPayload()
        if include_optional:
            return SystemconfigurationGetObjectV2ResponseMPayload(
                obj_systemconfiguration = eZmaxApi.models.systemconfiguration_response_compound.systemconfiguration-ResponseCompound()
            )
        else:
            return SystemconfigurationGetObjectV2ResponseMPayload(
                obj_systemconfiguration = eZmaxApi.models.systemconfiguration_response_compound.systemconfiguration-ResponseCompound(),
        )
        """

    def testSystemconfigurationGetObjectV2ResponseMPayload(self):
        """Test SystemconfigurationGetObjectV2ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
