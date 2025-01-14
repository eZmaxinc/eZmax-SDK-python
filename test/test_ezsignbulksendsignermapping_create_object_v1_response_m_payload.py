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

from eZmaxApi.models.ezsignbulksendsignermapping_create_object_v1_response_m_payload import EzsignbulksendsignermappingCreateObjectV1ResponseMPayload

class TestEzsignbulksendsignermappingCreateObjectV1ResponseMPayload(unittest.TestCase):
    """EzsignbulksendsignermappingCreateObjectV1ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsignbulksendsignermappingCreateObjectV1ResponseMPayload:
        """Test EzsignbulksendsignermappingCreateObjectV1ResponseMPayload
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsignbulksendsignermappingCreateObjectV1ResponseMPayload`
        """
        model = EzsignbulksendsignermappingCreateObjectV1ResponseMPayload()
        if include_optional:
            return EzsignbulksendsignermappingCreateObjectV1ResponseMPayload(
                a_pki_ezsignbulksendsignermapping_id = [
                    57
                    ]
            )
        else:
            return EzsignbulksendsignermappingCreateObjectV1ResponseMPayload(
                a_pki_ezsignbulksendsignermapping_id = [
                    57
                    ],
        )
        """

    def testEzsignbulksendsignermappingCreateObjectV1ResponseMPayload(self):
        """Test EzsignbulksendsignermappingCreateObjectV1ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
