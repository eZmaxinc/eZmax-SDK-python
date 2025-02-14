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

from eZmaxApi.models.ezsigntemplatedocument_patch_object_v1_request import EzsigntemplatedocumentPatchObjectV1Request

class TestEzsigntemplatedocumentPatchObjectV1Request(unittest.TestCase):
    """EzsigntemplatedocumentPatchObjectV1Request unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsigntemplatedocumentPatchObjectV1Request:
        """Test EzsigntemplatedocumentPatchObjectV1Request
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsigntemplatedocumentPatchObjectV1Request`
        """
        model = EzsigntemplatedocumentPatchObjectV1Request()
        if include_optional:
            return EzsigntemplatedocumentPatchObjectV1Request(
                obj_ezsigntemplatedocument = eZmaxApi.models.ezsigntemplatedocument_request_patch.ezsigntemplatedocument-RequestPatch(
                    s_ezsigntemplatedocument_name = 'Standard Contract', )
            )
        else:
            return EzsigntemplatedocumentPatchObjectV1Request(
                obj_ezsigntemplatedocument = eZmaxApi.models.ezsigntemplatedocument_request_patch.ezsigntemplatedocument-RequestPatch(
                    s_ezsigntemplatedocument_name = 'Standard Contract', ),
        )
        """

    def testEzsigntemplatedocumentPatchObjectV1Request(self):
        """Test EzsigntemplatedocumentPatchObjectV1Request"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
