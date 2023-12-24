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

from eZmaxApi.models.custom_ezsignfoldersignerassociationstatus_response import CustomEzsignfoldersignerassociationstatusResponse

class TestCustomEzsignfoldersignerassociationstatusResponse(unittest.TestCase):
    """CustomEzsignfoldersignerassociationstatusResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CustomEzsignfoldersignerassociationstatusResponse:
        """Test CustomEzsignfoldersignerassociationstatusResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CustomEzsignfoldersignerassociationstatusResponse`
        """
        model = CustomEzsignfoldersignerassociationstatusResponse()
        if include_optional:
            return CustomEzsignfoldersignerassociationstatusResponse(
                fki_ezsignfoldersignerassociation_id = 20,
                s_ezsignfoldersignerassociationstatus_lastname = 'Doe',
                s_ezsignfoldersignerassociationstatus_firstname = 'John',
                s_ezsignfoldersignerassociationstatus_description_x = 'John Doe',
                a_obj_ezsignsignaturestatus = [
                    eZmaxApi.models.custom_ezsignsignaturestatus_response.Custom-Ezsignsignaturestatus-Response(
                        e_ezsignsignaturestatus_steptype = 'Form', 
                        i_ezsignsignaturestatus_step = 1, 
                        i_ezsignsignaturestatus_total = 2, 
                        i_ezsignsignaturestatus_signed = 1, )
                    ]
            )
        else:
            return CustomEzsignfoldersignerassociationstatusResponse(
                fki_ezsignfoldersignerassociation_id = 20,
                a_obj_ezsignsignaturestatus = [
                    eZmaxApi.models.custom_ezsignsignaturestatus_response.Custom-Ezsignsignaturestatus-Response(
                        e_ezsignsignaturestatus_steptype = 'Form', 
                        i_ezsignsignaturestatus_step = 1, 
                        i_ezsignsignaturestatus_total = 2, 
                        i_ezsignsignaturestatus_signed = 1, )
                    ],
        )
        """

    def testCustomEzsignfoldersignerassociationstatusResponse(self):
        """Test CustomEzsignfoldersignerassociationstatusResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
