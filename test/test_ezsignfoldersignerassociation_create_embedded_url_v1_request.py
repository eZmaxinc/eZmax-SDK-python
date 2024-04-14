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

from eZmaxApi.models.ezsignfoldersignerassociation_create_embedded_url_v1_request import EzsignfoldersignerassociationCreateEmbeddedUrlV1Request

class TestEzsignfoldersignerassociationCreateEmbeddedUrlV1Request(unittest.TestCase):
    """EzsignfoldersignerassociationCreateEmbeddedUrlV1Request unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsignfoldersignerassociationCreateEmbeddedUrlV1Request:
        """Test EzsignfoldersignerassociationCreateEmbeddedUrlV1Request
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsignfoldersignerassociationCreateEmbeddedUrlV1Request`
        """
        model = EzsignfoldersignerassociationCreateEmbeddedUrlV1Request()
        if include_optional:
            return EzsignfoldersignerassociationCreateEmbeddedUrlV1Request(
                s_return_url = 'Https://www.example.com',
                s_iframedomain = '*.example.com',
                b_is_iframe = True
            )
        else:
            return EzsignfoldersignerassociationCreateEmbeddedUrlV1Request(
        )
        """

    def testEzsignfoldersignerassociationCreateEmbeddedUrlV1Request(self):
        """Test EzsignfoldersignerassociationCreateEmbeddedUrlV1Request"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
