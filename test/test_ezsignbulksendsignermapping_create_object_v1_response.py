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

from eZmaxApi.models.ezsignbulksendsignermapping_create_object_v1_response import EzsignbulksendsignermappingCreateObjectV1Response

class TestEzsignbulksendsignermappingCreateObjectV1Response(unittest.TestCase):
    """EzsignbulksendsignermappingCreateObjectV1Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsignbulksendsignermappingCreateObjectV1Response:
        """Test EzsignbulksendsignermappingCreateObjectV1Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsignbulksendsignermappingCreateObjectV1Response`
        """
        model = EzsignbulksendsignermappingCreateObjectV1Response()
        if include_optional:
            return EzsignbulksendsignermappingCreateObjectV1Response(
                m_payload = eZmaxApi.models.ezsignbulksendsignermapping_create_object_v1_response_m_payload.ezsignbulksendsignermapping-createObject-v1-Response-mPayload(
                    a_pki_ezsignbulksendsignermapping_id = [
                        57
                        ], )
            )
        else:
            return EzsignbulksendsignermappingCreateObjectV1Response(
                m_payload = eZmaxApi.models.ezsignbulksendsignermapping_create_object_v1_response_m_payload.ezsignbulksendsignermapping-createObject-v1-Response-mPayload(
                    a_pki_ezsignbulksendsignermapping_id = [
                        57
                        ], ),
        )
        """

    def testEzsignbulksendsignermappingCreateObjectV1Response(self):
        """Test EzsignbulksendsignermappingCreateObjectV1Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
