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

from eZmaxApi.models.contact_request_v2 import ContactRequestV2

class TestContactRequestV2(unittest.TestCase):
    """ContactRequestV2 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ContactRequestV2:
        """Test ContactRequestV2
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ContactRequestV2`
        """
        model = ContactRequestV2()
        if include_optional:
            return ContactRequestV2(
                fki_contacttitle_id = 2,
                fki_language_id = 2,
                e_contact_type = 'Agent',
                s_contact_firstname = 'John',
                s_contact_lastname = 'Doe',
                s_contact_company = 'eZmax Solutions Inc.',
                dt_contact_birthdate = '1980-01-01',
                s_contact_occupation = 'Programmer',
                t_contact_note = 'This is a note',
                b_contact_isactive = True,
                obj_contactinformations = eZmaxApi.models.contactinformations_request_compound.contactinformations-RequestCompound()
            )
        else:
            return ContactRequestV2(
                fki_contacttitle_id = 2,
                fki_language_id = 2,
                e_contact_type = 'Agent',
                s_contact_firstname = 'John',
                s_contact_lastname = 'Doe',
                obj_contactinformations = eZmaxApi.models.contactinformations_request_compound.contactinformations-RequestCompound(),
        )
        """

    def testContactRequestV2(self):
        """Test ContactRequestV2"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
