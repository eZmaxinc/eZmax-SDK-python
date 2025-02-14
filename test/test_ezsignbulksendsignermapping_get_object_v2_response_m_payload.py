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

from eZmaxApi.models.ezsignbulksendsignermapping_get_object_v2_response_m_payload import EzsignbulksendsignermappingGetObjectV2ResponseMPayload

class TestEzsignbulksendsignermappingGetObjectV2ResponseMPayload(unittest.TestCase):
    """EzsignbulksendsignermappingGetObjectV2ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsignbulksendsignermappingGetObjectV2ResponseMPayload:
        """Test EzsignbulksendsignermappingGetObjectV2ResponseMPayload
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsignbulksendsignermappingGetObjectV2ResponseMPayload`
        """
        model = EzsignbulksendsignermappingGetObjectV2ResponseMPayload()
        if include_optional:
            return EzsignbulksendsignermappingGetObjectV2ResponseMPayload(
                obj_ezsignbulksendsignermapping = eZmaxApi.models.ezsignbulksendsignermapping_response_compound.ezsignbulksendsignermapping-ResponseCompound()
            )
        else:
            return EzsignbulksendsignermappingGetObjectV2ResponseMPayload(
                obj_ezsignbulksendsignermapping = eZmaxApi.models.ezsignbulksendsignermapping_response_compound.ezsignbulksendsignermapping-ResponseCompound(),
        )
        """

    def testEzsignbulksendsignermappingGetObjectV2ResponseMPayload(self):
        """Test EzsignbulksendsignermappingGetObjectV2ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
