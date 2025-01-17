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

from eZmaxApi.models.variableexpense_get_object_v2_response import VariableexpenseGetObjectV2Response

class TestVariableexpenseGetObjectV2Response(unittest.TestCase):
    """VariableexpenseGetObjectV2Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VariableexpenseGetObjectV2Response:
        """Test VariableexpenseGetObjectV2Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VariableexpenseGetObjectV2Response`
        """
        model = VariableexpenseGetObjectV2Response()
        if include_optional:
            return VariableexpenseGetObjectV2Response(
                m_payload = eZmaxApi.models.variableexpense_get_object_v2_response_m_payload.variableexpense-getObject-v2-Response-mPayload(
                    obj_variableexpense = eZmaxApi.models.variableexpense_response_compound.variableexpense-ResponseCompound(), )
            )
        else:
            return VariableexpenseGetObjectV2Response(
                m_payload = eZmaxApi.models.variableexpense_get_object_v2_response_m_payload.variableexpense-getObject-v2-Response-mPayload(
                    obj_variableexpense = eZmaxApi.models.variableexpense_response_compound.variableexpense-ResponseCompound(), ),
        )
        """

    def testVariableexpenseGetObjectV2Response(self):
        """Test VariableexpenseGetObjectV2Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
