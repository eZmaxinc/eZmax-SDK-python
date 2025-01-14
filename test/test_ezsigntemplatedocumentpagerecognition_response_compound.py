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

from eZmaxApi.models.ezsigntemplatedocumentpagerecognition_response_compound import EzsigntemplatedocumentpagerecognitionResponseCompound

class TestEzsigntemplatedocumentpagerecognitionResponseCompound(unittest.TestCase):
    """EzsigntemplatedocumentpagerecognitionResponseCompound unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsigntemplatedocumentpagerecognitionResponseCompound:
        """Test EzsigntemplatedocumentpagerecognitionResponseCompound
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsigntemplatedocumentpagerecognitionResponseCompound`
        """
        model = EzsigntemplatedocumentpagerecognitionResponseCompound()
        if include_optional:
            return EzsigntemplatedocumentpagerecognitionResponseCompound(
                pki_ezsigntemplatedocumentpagerecognition_id = 126,
                fki_ezsigntemplatedocumentpage_id = 85,
                e_ezsigntemplatedocumentpagerecognition_operator = 'eq',
                e_ezsigntemplatedocumentpagerecognition_section = 'FirstLine',
                i_ezsigntemplatedocumentpagerecognition_similarpercentage = 50,
                i_ezsigntemplatedocumentpagerecognition_x = 36325,
                i_ezsigntemplatedocumentpagerecognition_y = 407,
                i_ezsigntemplatedocumentpagerecognition_width = 29232,
                i_ezsigntemplatedocumentpagerecognition_height = 42651,
                t_ezsigntemplatedocumentpagerecognition_text = 'Contract'
            )
        else:
            return EzsigntemplatedocumentpagerecognitionResponseCompound(
                pki_ezsigntemplatedocumentpagerecognition_id = 126,
                fki_ezsigntemplatedocumentpage_id = 85,
                e_ezsigntemplatedocumentpagerecognition_operator = 'eq',
                e_ezsigntemplatedocumentpagerecognition_section = 'FirstLine',
                t_ezsigntemplatedocumentpagerecognition_text = 'Contract',
        )
        """

    def testEzsigntemplatedocumentpagerecognitionResponseCompound(self):
        """Test EzsigntemplatedocumentpagerecognitionResponseCompound"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
