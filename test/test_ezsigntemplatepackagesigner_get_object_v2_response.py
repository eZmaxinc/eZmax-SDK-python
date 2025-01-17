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

from eZmaxApi.models.ezsigntemplatepackagesigner_get_object_v2_response import EzsigntemplatepackagesignerGetObjectV2Response

class TestEzsigntemplatepackagesignerGetObjectV2Response(unittest.TestCase):
    """EzsigntemplatepackagesignerGetObjectV2Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsigntemplatepackagesignerGetObjectV2Response:
        """Test EzsigntemplatepackagesignerGetObjectV2Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsigntemplatepackagesignerGetObjectV2Response`
        """
        model = EzsigntemplatepackagesignerGetObjectV2Response()
        if include_optional:
            return EzsigntemplatepackagesignerGetObjectV2Response(
                m_payload = eZmaxApi.models.ezsigntemplatepackagesigner_get_object_v2_response_m_payload.ezsigntemplatepackagesigner-getObject-v2-Response-mPayload(
                    obj_ezsigntemplatepackagesigner = eZmaxApi.models.ezsigntemplatepackagesigner_response_compound.ezsigntemplatepackagesigner-ResponseCompound(), )
            )
        else:
            return EzsigntemplatepackagesignerGetObjectV2Response(
                m_payload = eZmaxApi.models.ezsigntemplatepackagesigner_get_object_v2_response_m_payload.ezsigntemplatepackagesigner-getObject-v2-Response-mPayload(
                    obj_ezsigntemplatepackagesigner = eZmaxApi.models.ezsigntemplatepackagesigner_response_compound.ezsigntemplatepackagesigner-ResponseCompound(), ),
        )
        """

    def testEzsigntemplatepackagesignerGetObjectV2Response(self):
        """Test EzsigntemplatepackagesignerGetObjectV2Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
