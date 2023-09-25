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

from eZmaxApi.models.ezsigntemplatepackagemembership_get_object_v2_response_m_payload import EzsigntemplatepackagemembershipGetObjectV2ResponseMPayload  # noqa: E501

class TestEzsigntemplatepackagemembershipGetObjectV2ResponseMPayload(unittest.TestCase):
    """EzsigntemplatepackagemembershipGetObjectV2ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsigntemplatepackagemembershipGetObjectV2ResponseMPayload:
        """Test EzsigntemplatepackagemembershipGetObjectV2ResponseMPayload
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsigntemplatepackagemembershipGetObjectV2ResponseMPayload`
        """
        model = EzsigntemplatepackagemembershipGetObjectV2ResponseMPayload()  # noqa: E501
        if include_optional:
            return EzsigntemplatepackagemembershipGetObjectV2ResponseMPayload(
                obj_ezsigntemplatepackagemembership = eZmaxApi.models.ezsigntemplatepackagemembership_response_compound.ezsigntemplatepackagemembership-ResponseCompound()
            )
        else:
            return EzsigntemplatepackagemembershipGetObjectV2ResponseMPayload(
                obj_ezsigntemplatepackagemembership = eZmaxApi.models.ezsigntemplatepackagemembership_response_compound.ezsigntemplatepackagemembership-ResponseCompound(),
        )
        """

    def testEzsigntemplatepackagemembershipGetObjectV2ResponseMPayload(self):
        """Test EzsigntemplatepackagemembershipGetObjectV2ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
