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

from eZmaxApi.models.supply_response import SupplyResponse

class TestSupplyResponse(unittest.TestCase):
    """SupplyResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SupplyResponse:
        """Test SupplyResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SupplyResponse`
        """
        model = SupplyResponse()
        if include_optional:
            return SupplyResponse(
                pki_supply_id = 85,
                fki_glaccount_id = 35,
                fki_glaccountcontainer_id = 66,
                fki_variableexpense_id = 2,
                s_supply_code = 'PPLET',
                obj_supply_description = eZmaxApi.models.multilingual_supply_description.Multilingual-SupplyDescription(
                    s_supply_description1 = 'Papier lettre paquet', 
                    s_supply_description2 = 'Letter paper package', ),
                d_supply_unitprice = '8.00',
                b_supply_isactive = True,
                b_supply_variableprice = True,
                s_glaccount_description_x = 'Supplies income',
                s_glaccountcontainer_longdescription_x = 'Quebec',
                s_variableexpense_description_x = 'Équipements de bureau'
            )
        else:
            return SupplyResponse(
                pki_supply_id = 85,
                fki_variableexpense_id = 2,
                s_supply_code = 'PPLET',
                obj_supply_description = eZmaxApi.models.multilingual_supply_description.Multilingual-SupplyDescription(
                    s_supply_description1 = 'Papier lettre paquet', 
                    s_supply_description2 = 'Letter paper package', ),
                d_supply_unitprice = '8.00',
                b_supply_isactive = True,
                b_supply_variableprice = True,
        )
        """

    def testSupplyResponse(self):
        """Test SupplyResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
