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

from eZmaxApi.models.ezsigntemplatedocument_flatten_v1_response import EzsigntemplatedocumentFlattenV1Response

class TestEzsigntemplatedocumentFlattenV1Response(unittest.TestCase):
    """EzsigntemplatedocumentFlattenV1Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsigntemplatedocumentFlattenV1Response:
        """Test EzsigntemplatedocumentFlattenV1Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsigntemplatedocumentFlattenV1Response`
        """
        model = EzsigntemplatedocumentFlattenV1Response()
        if include_optional:
            return EzsigntemplatedocumentFlattenV1Response(
            )
        else:
            return EzsigntemplatedocumentFlattenV1Response(
        )
        """

    def testEzsigntemplatedocumentFlattenV1Response(self):
        """Test EzsigntemplatedocumentFlattenV1Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
