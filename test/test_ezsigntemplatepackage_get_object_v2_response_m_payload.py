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

from eZmaxApi.models.ezsigntemplatepackage_get_object_v2_response_m_payload import EzsigntemplatepackageGetObjectV2ResponseMPayload

class TestEzsigntemplatepackageGetObjectV2ResponseMPayload(unittest.TestCase):
    """EzsigntemplatepackageGetObjectV2ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsigntemplatepackageGetObjectV2ResponseMPayload:
        """Test EzsigntemplatepackageGetObjectV2ResponseMPayload
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsigntemplatepackageGetObjectV2ResponseMPayload`
        """
        model = EzsigntemplatepackageGetObjectV2ResponseMPayload()
        if include_optional:
            return EzsigntemplatepackageGetObjectV2ResponseMPayload(
                obj_ezsigntemplatepackage = eZmaxApi.models.ezsigntemplatepackage_response_compound.ezsigntemplatepackage-ResponseCompound()
            )
        else:
            return EzsigntemplatepackageGetObjectV2ResponseMPayload(
                obj_ezsigntemplatepackage = eZmaxApi.models.ezsigntemplatepackage_response_compound.ezsigntemplatepackage-ResponseCompound(),
        )
        """

    def testEzsigntemplatepackageGetObjectV2ResponseMPayload(self):
        """Test EzsigntemplatepackageGetObjectV2ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
