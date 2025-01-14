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

from eZmaxApi.models.ezsigndocument_edit_ezsignannotations_v1_request import EzsigndocumentEditEzsignannotationsV1Request

class TestEzsigndocumentEditEzsignannotationsV1Request(unittest.TestCase):
    """EzsigndocumentEditEzsignannotationsV1Request unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsigndocumentEditEzsignannotationsV1Request:
        """Test EzsigndocumentEditEzsignannotationsV1Request
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsigndocumentEditEzsignannotationsV1Request`
        """
        model = EzsigndocumentEditEzsignannotationsV1Request()
        if include_optional:
            return EzsigndocumentEditEzsignannotationsV1Request(
                a_obj_ezsignannotation = [
                    eZmaxApi.models.ezsignannotation_request_compound.ezsignannotation-RequestCompound()
                    ]
            )
        else:
            return EzsigndocumentEditEzsignannotationsV1Request(
                a_obj_ezsignannotation = [
                    eZmaxApi.models.ezsignannotation_request_compound.ezsignannotation-RequestCompound()
                    ],
        )
        """

    def testEzsigndocumentEditEzsignannotationsV1Request(self):
        """Test EzsigndocumentEditEzsignannotationsV1Request"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
