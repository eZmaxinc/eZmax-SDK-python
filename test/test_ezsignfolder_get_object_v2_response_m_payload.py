# coding: utf-8

"""
    eZmax API Definition (Full)

    This API expose all the functionnalities for the eZmax and eZsign applications.

    The version of the OpenAPI document: 1.2.0
    Contact: support-api@ezmax.ca
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from eZmaxApi.models.ezsignfolder_get_object_v2_response_m_payload import EzsignfolderGetObjectV2ResponseMPayload  # noqa: E501

class TestEzsignfolderGetObjectV2ResponseMPayload(unittest.TestCase):
    """EzsignfolderGetObjectV2ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsignfolderGetObjectV2ResponseMPayload:
        """Test EzsignfolderGetObjectV2ResponseMPayload
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsignfolderGetObjectV2ResponseMPayload`
        """
        model = EzsignfolderGetObjectV2ResponseMPayload()  # noqa: E501
        if include_optional:
            return EzsignfolderGetObjectV2ResponseMPayload(
                obj_ezsignfolder = eZmaxApi.models.ezsignfolder_response_compound.ezsignfolder-ResponseCompound()
            )
        else:
            return EzsignfolderGetObjectV2ResponseMPayload(
                obj_ezsignfolder = eZmaxApi.models.ezsignfolder_response_compound.ezsignfolder-ResponseCompound(),
        )
        """

    def testEzsignfolderGetObjectV2ResponseMPayload(self):
        """Test EzsignfolderGetObjectV2ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
