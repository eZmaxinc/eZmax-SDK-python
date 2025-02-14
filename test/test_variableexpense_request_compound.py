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

from eZmaxApi.models.variableexpense_request_compound import VariableexpenseRequestCompound

class TestVariableexpenseRequestCompound(unittest.TestCase):
    """VariableexpenseRequestCompound unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VariableexpenseRequestCompound:
        """Test VariableexpenseRequestCompound
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VariableexpenseRequestCompound`
        """
        model = VariableexpenseRequestCompound()
        if include_optional:
            return VariableexpenseRequestCompound(
                pki_variableexpense_id = 2,
                s_variableexpense_code = 'EQBUR',
                obj_variableexpense_description = eZmaxApi.models.multilingual_variableexpense_description.Multilingual-VariableexpenseDescription(
                    s_variableexpense_description1 = 'Équipements de bureau', 
                    s_variableexpense_description2 = 'Office equipment', ),
                e_variableexpense_taxable = 'Yes',
                b_variableexpense_isactive = True
            )
        else:
            return VariableexpenseRequestCompound(
                s_variableexpense_code = 'EQBUR',
                obj_variableexpense_description = eZmaxApi.models.multilingual_variableexpense_description.Multilingual-VariableexpenseDescription(
                    s_variableexpense_description1 = 'Équipements de bureau', 
                    s_variableexpense_description2 = 'Office equipment', ),
                e_variableexpense_taxable = 'Yes',
                b_variableexpense_isactive = True,
        )
        """

    def testVariableexpenseRequestCompound(self):
        """Test VariableexpenseRequestCompound"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
