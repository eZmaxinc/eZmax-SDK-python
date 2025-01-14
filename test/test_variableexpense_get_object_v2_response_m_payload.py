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

from eZmaxApi.models.variableexpense_get_object_v2_response_m_payload import VariableexpenseGetObjectV2ResponseMPayload

class TestVariableexpenseGetObjectV2ResponseMPayload(unittest.TestCase):
    """VariableexpenseGetObjectV2ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VariableexpenseGetObjectV2ResponseMPayload:
        """Test VariableexpenseGetObjectV2ResponseMPayload
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VariableexpenseGetObjectV2ResponseMPayload`
        """
        model = VariableexpenseGetObjectV2ResponseMPayload()
        if include_optional:
            return VariableexpenseGetObjectV2ResponseMPayload(
                obj_variableexpense = eZmaxApi.models.variableexpense_response_compound.variableexpense-ResponseCompound()
            )
        else:
            return VariableexpenseGetObjectV2ResponseMPayload(
                obj_variableexpense = eZmaxApi.models.variableexpense_response_compound.variableexpense-ResponseCompound(),
        )
        """

    def testVariableexpenseGetObjectV2ResponseMPayload(self):
        """Test VariableexpenseGetObjectV2ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
