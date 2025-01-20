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

from eZmaxApi.models.ezsignfolder_create_object_v1_request import EzsignfolderCreateObjectV1Request

class TestEzsignfolderCreateObjectV1Request(unittest.TestCase):
    """EzsignfolderCreateObjectV1Request unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsignfolderCreateObjectV1Request:
        """Test EzsignfolderCreateObjectV1Request
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsignfolderCreateObjectV1Request`
        """
        model = EzsignfolderCreateObjectV1Request()
        if include_optional:
            return EzsignfolderCreateObjectV1Request(
                obj_ezsignfolder = eZmaxApi.models.ezsignfolder_request.ezsignfolder-Request(
                    pki_ezsignfolder_id = 33, 
                    fki_ezsignfoldertype_id = 5, 
                    fki_timezone_id = 247, 
                    fki_ezsigntsarequirement_id = 1, 
                    s_ezsignfolder_description = 'Test eZsign Folder', 
                    t_ezsignfolder_note = 'This is a note', 
                    e_ezsignfolder_sendreminderfrequency = 'None', 
                    s_ezsignfolder_externalid = '{"ID": 1234, "TAGS": ["tag1", "tag2", "tag3"]}', ),
                obj_ezsignfolder_compound = eZmaxApi.models.ezsignfolder_request.ezsignfolder-Request(
                    pki_ezsignfolder_id = 33, 
                    fki_ezsignfoldertype_id = 5, 
                    fki_timezone_id = 247, 
                    fki_ezsigntsarequirement_id = 1, 
                    s_ezsignfolder_description = 'Test eZsign Folder', 
                    t_ezsignfolder_note = 'This is a note', 
                    e_ezsignfolder_sendreminderfrequency = 'None', 
                    s_ezsignfolder_externalid = '{"ID": 1234, "TAGS": ["tag1", "tag2", "tag3"]}', )
            )
        else:
            return EzsignfolderCreateObjectV1Request(
        )
        """

    def testEzsignfolderCreateObjectV1Request(self):
        """Test EzsignfolderCreateObjectV1Request"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
