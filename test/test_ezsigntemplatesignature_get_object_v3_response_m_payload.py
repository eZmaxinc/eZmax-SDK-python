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

from eZmaxApi.models.ezsigntemplatesignature_get_object_v3_response_m_payload import EzsigntemplatesignatureGetObjectV3ResponseMPayload

class TestEzsigntemplatesignatureGetObjectV3ResponseMPayload(unittest.TestCase):
    """EzsigntemplatesignatureGetObjectV3ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsigntemplatesignatureGetObjectV3ResponseMPayload:
        """Test EzsigntemplatesignatureGetObjectV3ResponseMPayload
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsigntemplatesignatureGetObjectV3ResponseMPayload`
        """
        model = EzsigntemplatesignatureGetObjectV3ResponseMPayload()
        if include_optional:
            return EzsigntemplatesignatureGetObjectV3ResponseMPayload(
                obj_ezsigntemplatesignature = eZmaxApi.models.ezsigntemplatesignature_response_compound_v3.ezsigntemplatesignature-ResponseCompoundV3()
            )
        else:
            return EzsigntemplatesignatureGetObjectV3ResponseMPayload(
                obj_ezsigntemplatesignature = eZmaxApi.models.ezsigntemplatesignature_response_compound_v3.ezsigntemplatesignature-ResponseCompoundV3(),
        )
        """

    def testEzsigntemplatesignatureGetObjectV3ResponseMPayload(self):
        """Test EzsigntemplatesignatureGetObjectV3ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
