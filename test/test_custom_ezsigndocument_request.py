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

from eZmaxApi.models.custom_ezsigndocument_request import CustomEzsigndocumentRequest

class TestCustomEzsigndocumentRequest(unittest.TestCase):
    """CustomEzsigndocumentRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CustomEzsigndocumentRequest:
        """Test CustomEzsigndocumentRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CustomEzsigndocumentRequest`
        """
        model = CustomEzsigndocumentRequest()
        if include_optional:
            return CustomEzsigndocumentRequest(
                pki_ezsigndocument_id = 97,
                a_obj_ezsigndocumentdependency = [
                    eZmaxApi.models.ezsigndocumentdependency_request_compound.ezsigndocumentdependency-RequestCompound()
                    ]
            )
        else:
            return CustomEzsigndocumentRequest(
                pki_ezsigndocument_id = 97,
                a_obj_ezsigndocumentdependency = [
                    eZmaxApi.models.ezsigndocumentdependency_request_compound.ezsigndocumentdependency-RequestCompound()
                    ],
        )
        """

    def testCustomEzsigndocumentRequest(self):
        """Test CustomEzsigndocumentRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
