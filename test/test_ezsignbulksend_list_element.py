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

from eZmaxApi.models.ezsignbulksend_list_element import EzsignbulksendListElement

class TestEzsignbulksendListElement(unittest.TestCase):
    """EzsignbulksendListElement unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsignbulksendListElement:
        """Test EzsignbulksendListElement
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsignbulksendListElement`
        """
        model = EzsignbulksendListElement()
        if include_optional:
            return EzsignbulksendListElement(
                pki_ezsignbulksend_id = 8,
                fki_ezsignfoldertype_id = 5,
                s_ezsignbulksend_description = 'Test eZsign Bulk Send',
                s_ezsignfoldertype_name_x = 'Default',
                b_ezsignbulksend_needvalidation = True,
                i_ezsignbulksendtransmission = 56,
                i_ezsignfolder = 56,
                i_ezsigndocument = 56,
                i_ezsignsignature = 56,
                i_ezsignsignature_signed = 56,
                b_ezsignbulksend_isactive = True
            )
        else:
            return EzsignbulksendListElement(
                pki_ezsignbulksend_id = 8,
                fki_ezsignfoldertype_id = 5,
                s_ezsignbulksend_description = 'Test eZsign Bulk Send',
                s_ezsignfoldertype_name_x = 'Default',
                b_ezsignbulksend_needvalidation = True,
                i_ezsignbulksendtransmission = 56,
                i_ezsignfolder = 56,
                i_ezsigndocument = 56,
                i_ezsignsignature = 56,
                i_ezsignsignature_signed = 56,
                b_ezsignbulksend_isactive = True,
        )
        """

    def testEzsignbulksendListElement(self):
        """Test EzsignbulksendListElement"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
