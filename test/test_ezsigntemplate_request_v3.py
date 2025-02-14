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

from eZmaxApi.models.ezsigntemplate_request_v3 import EzsigntemplateRequestV3

class TestEzsigntemplateRequestV3(unittest.TestCase):
    """EzsigntemplateRequestV3 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsigntemplateRequestV3:
        """Test EzsigntemplateRequestV3
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsigntemplateRequestV3`
        """
        model = EzsigntemplateRequestV3()
        if include_optional:
            return EzsigntemplateRequestV3(
                pki_ezsigntemplate_id = 36,
                fki_ezsignfoldertype_id = 5,
                fki_language_id = 2,
                fki_ezdoctemplatedocument_id = 95,
                s_ezsigntemplate_description = 'Standard Contract',
                s_ezsigntemplate_externaldescription = 'Test eZsign Folder',
                t_ezsigntemplate_comment = '',
                e_ezsigntemplate_recognition = 'No',
                s_ezsigntemplate_filenameregexp = 'Contract',
                b_ezsigntemplate_adminonly = True,
                e_ezsigntemplate_type = 'Ezsignfoldertype'
            )
        else:
            return EzsigntemplateRequestV3(
                fki_language_id = 2,
                s_ezsigntemplate_description = 'Standard Contract',
                b_ezsigntemplate_adminonly = True,
                e_ezsigntemplate_type = 'Ezsignfoldertype',
        )
        """

    def testEzsigntemplateRequestV3(self):
        """Test EzsigntemplateRequestV3"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
