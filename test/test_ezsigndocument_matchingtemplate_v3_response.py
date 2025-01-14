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

from eZmaxApi.models.ezsigndocument_matchingtemplate_v3_response import EzsigndocumentMatchingtemplateV3Response

class TestEzsigndocumentMatchingtemplateV3Response(unittest.TestCase):
    """EzsigndocumentMatchingtemplateV3Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsigndocumentMatchingtemplateV3Response:
        """Test EzsigndocumentMatchingtemplateV3Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsigndocumentMatchingtemplateV3Response`
        """
        model = EzsigndocumentMatchingtemplateV3Response()
        if include_optional:
            return EzsigndocumentMatchingtemplateV3Response(
                pki_ezsigntemplate_id = 36,
                pki_ezsigntemplateglobal_id = 36
            )
        else:
            return EzsigndocumentMatchingtemplateV3Response(
        )
        """

    def testEzsigndocumentMatchingtemplateV3Response(self):
        """Test EzsigndocumentMatchingtemplateV3Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
