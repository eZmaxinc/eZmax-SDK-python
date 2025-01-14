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

from eZmaxApi.models.ezsignbulksend_get_ezsignbulksendtransmissions_v1_response_m_payload import EzsignbulksendGetEzsignbulksendtransmissionsV1ResponseMPayload

class TestEzsignbulksendGetEzsignbulksendtransmissionsV1ResponseMPayload(unittest.TestCase):
    """EzsignbulksendGetEzsignbulksendtransmissionsV1ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsignbulksendGetEzsignbulksendtransmissionsV1ResponseMPayload:
        """Test EzsignbulksendGetEzsignbulksendtransmissionsV1ResponseMPayload
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsignbulksendGetEzsignbulksendtransmissionsV1ResponseMPayload`
        """
        model = EzsignbulksendGetEzsignbulksendtransmissionsV1ResponseMPayload()
        if include_optional:
            return EzsignbulksendGetEzsignbulksendtransmissionsV1ResponseMPayload(
                a_obj_ezsignbulksendtransmission = [
                    eZmaxApi.models.ezsignbulksendtransmission_response_compound.ezsignbulksendtransmission-ResponseCompound()
                    ]
            )
        else:
            return EzsignbulksendGetEzsignbulksendtransmissionsV1ResponseMPayload(
                a_obj_ezsignbulksendtransmission = [
                    eZmaxApi.models.ezsignbulksendtransmission_response_compound.ezsignbulksendtransmission-ResponseCompound()
                    ],
        )
        """

    def testEzsignbulksendGetEzsignbulksendtransmissionsV1ResponseMPayload(self):
        """Test EzsignbulksendGetEzsignbulksendtransmissionsV1ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
