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

from eZmaxApi.models.ezsignannotation_response import EzsignannotationResponse

class TestEzsignannotationResponse(unittest.TestCase):
    """EzsignannotationResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsignannotationResponse:
        """Test EzsignannotationResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsignannotationResponse`
        """
        model = EzsignannotationResponse()
        if include_optional:
            return EzsignannotationResponse(
                pki_ezsignannotation_id = 113,
                fki_ezsigndocument_id = 97,
                e_ezsignannotation_horizontalalignment = 'Center',
                e_ezsignannotation_verticalalignment = 'Bottom',
                e_ezsignannotation_type = 'Text',
                i_ezsignannotation_x = 50,
                i_ezsignannotation_y = 50,
                i_ezsignannotation_width = 75,
                i_ezsignannotation_height = 25,
                s_ezsignannotation_text = 'Sample',
                i_ezsignpage_pagenumber = 1
            )
        else:
            return EzsignannotationResponse(
                pki_ezsignannotation_id = 113,
                fki_ezsigndocument_id = 97,
                e_ezsignannotation_type = 'Text',
                i_ezsignannotation_x = 50,
                i_ezsignannotation_y = 50,
                i_ezsignpage_pagenumber = 1,
        )
        """

    def testEzsignannotationResponse(self):
        """Test EzsignannotationResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
