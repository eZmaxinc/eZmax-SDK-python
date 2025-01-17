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

from eZmaxApi.models.ezsigndocument_get_object_v1_response import EzsigndocumentGetObjectV1Response

class TestEzsigndocumentGetObjectV1Response(unittest.TestCase):
    """EzsigndocumentGetObjectV1Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsigndocumentGetObjectV1Response:
        """Test EzsigndocumentGetObjectV1Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsigndocumentGetObjectV1Response`
        """
        model = EzsigndocumentGetObjectV1Response()
        if include_optional:
            return EzsigndocumentGetObjectV1Response(
                m_payload = eZmaxApi.models.ezsigndocument_response_compound.ezsigndocument-ResponseCompound()
            )
        else:
            return EzsigndocumentGetObjectV1Response(
                m_payload = eZmaxApi.models.ezsigndocument_response_compound.ezsigndocument-ResponseCompound(),
        )
        """

    def testEzsigndocumentGetObjectV1Response(self):
        """Test EzsigndocumentGetObjectV1Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
