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

from eZmaxApi.models.ezsigntemplatepackagemembership_create_object_v1_request import EzsigntemplatepackagemembershipCreateObjectV1Request

class TestEzsigntemplatepackagemembershipCreateObjectV1Request(unittest.TestCase):
    """EzsigntemplatepackagemembershipCreateObjectV1Request unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsigntemplatepackagemembershipCreateObjectV1Request:
        """Test EzsigntemplatepackagemembershipCreateObjectV1Request
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsigntemplatepackagemembershipCreateObjectV1Request`
        """
        model = EzsigntemplatepackagemembershipCreateObjectV1Request()
        if include_optional:
            return EzsigntemplatepackagemembershipCreateObjectV1Request(
                a_obj_ezsigntemplatepackagemembership = [
                    eZmaxApi.models.ezsigntemplatepackagemembership_request_compound.ezsigntemplatepackagemembership-RequestCompound()
                    ]
            )
        else:
            return EzsigntemplatepackagemembershipCreateObjectV1Request(
                a_obj_ezsigntemplatepackagemembership = [
                    eZmaxApi.models.ezsigntemplatepackagemembership_request_compound.ezsigntemplatepackagemembership-RequestCompound()
                    ],
        )
        """

    def testEzsigntemplatepackagemembershipCreateObjectV1Request(self):
        """Test EzsigntemplatepackagemembershipCreateObjectV1Request"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
