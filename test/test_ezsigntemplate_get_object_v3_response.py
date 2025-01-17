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

from eZmaxApi.models.ezsigntemplate_get_object_v3_response import EzsigntemplateGetObjectV3Response

class TestEzsigntemplateGetObjectV3Response(unittest.TestCase):
    """EzsigntemplateGetObjectV3Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsigntemplateGetObjectV3Response:
        """Test EzsigntemplateGetObjectV3Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsigntemplateGetObjectV3Response`
        """
        model = EzsigntemplateGetObjectV3Response()
        if include_optional:
            return EzsigntemplateGetObjectV3Response(
                m_payload = eZmaxApi.models.ezsigntemplate_get_object_v3_response_m_payload.ezsigntemplate-getObject-v3-Response-mPayload(
                    obj_ezsigntemplate = eZmaxApi.models.ezsigntemplate_response_compound_v3.ezsigntemplate-ResponseCompoundV3(), )
            )
        else:
            return EzsigntemplateGetObjectV3Response(
                m_payload = eZmaxApi.models.ezsigntemplate_get_object_v3_response_m_payload.ezsigntemplate-getObject-v3-Response-mPayload(
                    obj_ezsigntemplate = eZmaxApi.models.ezsigntemplate_response_compound_v3.ezsigntemplate-ResponseCompoundV3(), ),
        )
        """

    def testEzsigntemplateGetObjectV3Response(self):
        """Test EzsigntemplateGetObjectV3Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
