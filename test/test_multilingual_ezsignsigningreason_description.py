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

from eZmaxApi.models.multilingual_ezsignsigningreason_description import MultilingualEzsignsigningreasonDescription

class TestMultilingualEzsignsigningreasonDescription(unittest.TestCase):
    """MultilingualEzsignsigningreasonDescription unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MultilingualEzsignsigningreasonDescription:
        """Test MultilingualEzsignsigningreasonDescription
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MultilingualEzsignsigningreasonDescription`
        """
        model = MultilingualEzsignsigningreasonDescription()
        if include_optional:
            return MultilingualEzsignsigningreasonDescription(
                s_ezsignsigningreason_description1 = 'J'approuve ce document',
                s_ezsignsigningreason_description2 = 'I approve this document'
            )
        else:
            return MultilingualEzsignsigningreasonDescription(
        )
        """

    def testMultilingualEzsignsigningreasonDescription(self):
        """Test MultilingualEzsignsigningreasonDescription"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()