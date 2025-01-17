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

from eZmaxApi.models.ezsignsigner_response_compound import EzsignsignerResponseCompound

class TestEzsignsignerResponseCompound(unittest.TestCase):
    """EzsignsignerResponseCompound unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsignsignerResponseCompound:
        """Test EzsignsignerResponseCompound
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsignsignerResponseCompound`
        """
        model = EzsignsignerResponseCompound()
        if include_optional:
            return EzsignsignerResponseCompound(
                obj_contact = eZmaxApi.models.ezsignsigner_response_compound_contact.ezsignsigner-ResponseCompound-Contact(
                    pki_contact_id = 21, 
                    s_contact_firstname = 'John', 
                    s_contact_lastname = 'Doe', 
                    fki_language_id = 2, 
                    s_email_address = 'email@example.com', 
                    s_phone_e164 = '+15149901516', 
                    s_phone_extension = '123', 
                    s_phone_e164_cell = '+15149901516', )
            )
        else:
            return EzsignsignerResponseCompound(
                obj_contact = eZmaxApi.models.ezsignsigner_response_compound_contact.ezsignsigner-ResponseCompound-Contact(
                    pki_contact_id = 21, 
                    s_contact_firstname = 'John', 
                    s_contact_lastname = 'Doe', 
                    fki_language_id = 2, 
                    s_email_address = 'email@example.com', 
                    s_phone_e164 = '+15149901516', 
                    s_phone_extension = '123', 
                    s_phone_e164_cell = '+15149901516', ),
        )
        """

    def testEzsignsignerResponseCompound(self):
        """Test EzsignsignerResponseCompound"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
