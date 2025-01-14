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

from eZmaxApi.models.ezmaxinvoicing_get_object_v2_response_m_payload import EzmaxinvoicingGetObjectV2ResponseMPayload

class TestEzmaxinvoicingGetObjectV2ResponseMPayload(unittest.TestCase):
    """EzmaxinvoicingGetObjectV2ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzmaxinvoicingGetObjectV2ResponseMPayload:
        """Test EzmaxinvoicingGetObjectV2ResponseMPayload
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzmaxinvoicingGetObjectV2ResponseMPayload`
        """
        model = EzmaxinvoicingGetObjectV2ResponseMPayload()
        if include_optional:
            return EzmaxinvoicingGetObjectV2ResponseMPayload(
                obj_ezmaxinvoicing = eZmaxApi.models.ezmaxinvoicing_response_compound.ezmaxinvoicing-ResponseCompound()
            )
        else:
            return EzmaxinvoicingGetObjectV2ResponseMPayload(
                obj_ezmaxinvoicing = eZmaxApi.models.ezmaxinvoicing_response_compound.ezmaxinvoicing-ResponseCompound(),
        )
        """

    def testEzmaxinvoicingGetObjectV2ResponseMPayload(self):
        """Test EzmaxinvoicingGetObjectV2ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
