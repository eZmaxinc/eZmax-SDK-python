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

from eZmaxApi.models.ezsignfoldertype_get_object_v3_response_m_payload import EzsignfoldertypeGetObjectV3ResponseMPayload

class TestEzsignfoldertypeGetObjectV3ResponseMPayload(unittest.TestCase):
    """EzsignfoldertypeGetObjectV3ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsignfoldertypeGetObjectV3ResponseMPayload:
        """Test EzsignfoldertypeGetObjectV3ResponseMPayload
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsignfoldertypeGetObjectV3ResponseMPayload`
        """
        model = EzsignfoldertypeGetObjectV3ResponseMPayload()
        if include_optional:
            return EzsignfoldertypeGetObjectV3ResponseMPayload(
                obj_ezsignfoldertype = eZmaxApi.models.ezsignfoldertype_response_compound_v3.ezsignfoldertype-ResponseCompoundV3()
            )
        else:
            return EzsignfoldertypeGetObjectV3ResponseMPayload(
                obj_ezsignfoldertype = eZmaxApi.models.ezsignfoldertype_response_compound_v3.ezsignfoldertype-ResponseCompoundV3(),
        )
        """

    def testEzsignfoldertypeGetObjectV3ResponseMPayload(self):
        """Test EzsignfoldertypeGetObjectV3ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()