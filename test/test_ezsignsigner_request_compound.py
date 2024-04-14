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

from eZmaxApi.models.ezsignsigner_request_compound import EzsignsignerRequestCompound

class TestEzsignsignerRequestCompound(unittest.TestCase):
    """EzsignsignerRequestCompound unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsignsignerRequestCompound:
        """Test EzsignsignerRequestCompound
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsignsignerRequestCompound`
        """
        model = EzsignsignerRequestCompound()
        if include_optional:
            return EzsignsignerRequestCompound(
                fki_userlogintype_id = 2,
                fki_taxassignment_id = 1,
                fki_secretquestion_id = 7,
                e_ezsignsigner_logintype = 'Password',
                s_ezsignsigner_secretanswer = '',
                obj_contact = eZmaxApi.models.ezsignsigner_request_compound_contact.ezsignsigner-RequestCompound-Contact(
                    s_contact_firstname = 'John', 
                    s_contact_lastname = 'Doe', 
                    fki_language_id = 2, 
                    s_email_address = 'email@example.com', 
                    s_phone_e164 = '+15149901516', 
                    s_phone_extension = '123', 
                    s_phone_e164_cell = '+15149901516', 
                    s_phone_number = '', 
                    s_phone_number_cell = '', )
            )
        else:
            return EzsignsignerRequestCompound(
                fki_taxassignment_id = 1,
                obj_contact = eZmaxApi.models.ezsignsigner_request_compound_contact.ezsignsigner-RequestCompound-Contact(
                    s_contact_firstname = 'John', 
                    s_contact_lastname = 'Doe', 
                    fki_language_id = 2, 
                    s_email_address = 'email@example.com', 
                    s_phone_e164 = '+15149901516', 
                    s_phone_extension = '123', 
                    s_phone_e164_cell = '+15149901516', 
                    s_phone_number = '', 
                    s_phone_number_cell = '', ),
        )
        """

    def testEzsignsignerRequestCompound(self):
        """Test EzsignsignerRequestCompound"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
