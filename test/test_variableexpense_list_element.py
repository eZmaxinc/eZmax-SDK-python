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
import datetime

from eZmaxApi.models.variableexpense_list_element import VariableexpenseListElement

class TestVariableexpenseListElement(unittest.TestCase):
    """VariableexpenseListElement unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VariableexpenseListElement:
        """Test VariableexpenseListElement
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VariableexpenseListElement`
        """
        model = VariableexpenseListElement()
        if include_optional:
            return VariableexpenseListElement(
                pki_variableexpense_id = 2,
                s_variableexpense_code = 'EQBUR',
                s_variableexpense_description_x = 'Équipements de bureau',
                e_variableexpense_taxable = 'Yes',
                b_variableexpense_isactive = True
            )
        else:
            return VariableexpenseListElement(
                pki_variableexpense_id = 2,
        )
        """

    def testVariableexpenseListElement(self):
        """Test VariableexpenseListElement"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
