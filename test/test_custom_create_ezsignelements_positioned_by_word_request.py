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

from eZmaxApi.models.custom_create_ezsignelements_positioned_by_word_request import CustomCreateEzsignelementsPositionedByWordRequest

class TestCustomCreateEzsignelementsPositionedByWordRequest(unittest.TestCase):
    """CustomCreateEzsignelementsPositionedByWordRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CustomCreateEzsignelementsPositionedByWordRequest:
        """Test CustomCreateEzsignelementsPositionedByWordRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CustomCreateEzsignelementsPositionedByWordRequest`
        """
        model = CustomCreateEzsignelementsPositionedByWordRequest()
        if include_optional:
            return CustomCreateEzsignelementsPositionedByWordRequest(
                s_createezsignelementspositionedbyword_pattern = 'jUR,rZ#UM/?R,Fp^l6$AR',
                i_createezsignelementspositionedbyword_offsetx = 56,
                i_createezsignelementspositionedbyword_offsety = 56,
                e_createezsignelementspositionedbyword_occurance = 'All'
            )
        else:
            return CustomCreateEzsignelementsPositionedByWordRequest(
                s_createezsignelementspositionedbyword_pattern = 'jUR,rZ#UM/?R,Fp^l6$AR',
                i_createezsignelementspositionedbyword_offsetx = 56,
                i_createezsignelementspositionedbyword_offsety = 56,
                e_createezsignelementspositionedbyword_occurance = 'All',
        )
        """

    def testCustomCreateEzsignelementsPositionedByWordRequest(self):
        """Test CustomCreateEzsignelementsPositionedByWordRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
