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

from eZmaxApi.models.multilingual_versionhistory_detail import MultilingualVersionhistoryDetail

class TestMultilingualVersionhistoryDetail(unittest.TestCase):
    """MultilingualVersionhistoryDetail unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MultilingualVersionhistoryDetail:
        """Test MultilingualVersionhistoryDetail
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MultilingualVersionhistoryDetail`
        """
        model = MultilingualVersionhistoryDetail()
        if include_optional:
            return MultilingualVersionhistoryDetail(
                t_versionhistory_detail1 = 'Message important',
                t_versionhistory_detail2 = 'Important message'
            )
        else:
            return MultilingualVersionhistoryDetail(
        )
        """

    def testMultilingualVersionhistoryDetail(self):
        """Test MultilingualVersionhistoryDetail"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
