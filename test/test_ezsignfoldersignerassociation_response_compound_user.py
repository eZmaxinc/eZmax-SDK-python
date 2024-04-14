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

from eZmaxApi.models.ezsignfoldersignerassociation_response_compound_user import EzsignfoldersignerassociationResponseCompoundUser

class TestEzsignfoldersignerassociationResponseCompoundUser(unittest.TestCase):
    """EzsignfoldersignerassociationResponseCompoundUser unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsignfoldersignerassociationResponseCompoundUser:
        """Test EzsignfoldersignerassociationResponseCompoundUser
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsignfoldersignerassociationResponseCompoundUser`
        """
        model = EzsignfoldersignerassociationResponseCompoundUser()
        if include_optional:
            return EzsignfoldersignerassociationResponseCompoundUser(
                pki_user_id = 70,
                fki_language_id = 2,
                s_user_firstname = 'John',
                s_user_lastname = 'Doe',
                s_email_address = 'email@example.com'
            )
        else:
            return EzsignfoldersignerassociationResponseCompoundUser(
                pki_user_id = 70,
                fki_language_id = 2,
                s_user_firstname = 'John',
                s_user_lastname = 'Doe',
                s_email_address = 'email@example.com',
        )
        """

    def testEzsignfoldersignerassociationResponseCompoundUser(self):
        """Test EzsignfoldersignerassociationResponseCompoundUser"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
