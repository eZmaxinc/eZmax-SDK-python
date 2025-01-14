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

from eZmaxApi.models.ezsignfolder_request_compound import EzsignfolderRequestCompound

class TestEzsignfolderRequestCompound(unittest.TestCase):
    """EzsignfolderRequestCompound unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsignfolderRequestCompound:
        """Test EzsignfolderRequestCompound
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsignfolderRequestCompound`
        """
        model = EzsignfolderRequestCompound()
        if include_optional:
            return EzsignfolderRequestCompound(
                pki_ezsignfolder_id = 33,
                fki_ezsignfoldertype_id = 5,
                fki_timezone_id = 247,
                fki_ezsigntsarequirement_id = 1,
                s_ezsignfolder_description = 'Test eZsign Folder',
                t_ezsignfolder_note = 'This is a note',
                e_ezsignfolder_sendreminderfrequency = 'None',
                s_ezsignfolder_externalid = '{"ID": 1234, "TAGS": ["tag1", "tag2", "tag3"]}'
            )
        else:
            return EzsignfolderRequestCompound(
                fki_ezsignfoldertype_id = 5,
                s_ezsignfolder_description = 'Test eZsign Folder',
                e_ezsignfolder_sendreminderfrequency = 'None',
        )
        """

    def testEzsignfolderRequestCompound(self):
        """Test EzsignfolderRequestCompound"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
