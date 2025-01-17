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

from eZmaxApi.models.ezsigntemplatedocumentpagerecognition_delete_object_v1_response import EzsigntemplatedocumentpagerecognitionDeleteObjectV1Response

class TestEzsigntemplatedocumentpagerecognitionDeleteObjectV1Response(unittest.TestCase):
    """EzsigntemplatedocumentpagerecognitionDeleteObjectV1Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsigntemplatedocumentpagerecognitionDeleteObjectV1Response:
        """Test EzsigntemplatedocumentpagerecognitionDeleteObjectV1Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsigntemplatedocumentpagerecognitionDeleteObjectV1Response`
        """
        model = EzsigntemplatedocumentpagerecognitionDeleteObjectV1Response()
        if include_optional:
            return EzsigntemplatedocumentpagerecognitionDeleteObjectV1Response(
            )
        else:
            return EzsigntemplatedocumentpagerecognitionDeleteObjectV1Response(
        )
        """

    def testEzsigntemplatedocumentpagerecognitionDeleteObjectV1Response(self):
        """Test EzsigntemplatedocumentpagerecognitionDeleteObjectV1Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
