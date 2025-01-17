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

from eZmaxApi.models.ezsigntemplatepackage_get_list_v1_response_m_payload import EzsigntemplatepackageGetListV1ResponseMPayload

class TestEzsigntemplatepackageGetListV1ResponseMPayload(unittest.TestCase):
    """EzsigntemplatepackageGetListV1ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsigntemplatepackageGetListV1ResponseMPayload:
        """Test EzsigntemplatepackageGetListV1ResponseMPayload
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsigntemplatepackageGetListV1ResponseMPayload`
        """
        model = EzsigntemplatepackageGetListV1ResponseMPayload()
        if include_optional:
            return EzsigntemplatepackageGetListV1ResponseMPayload(
                a_obj_ezsigntemplatepackage = [
                    eZmaxApi.models.ezsigntemplatepackage_list_element.ezsigntemplatepackage-ListElement(
                        pki_ezsigntemplatepackage_id = 99, 
                        fki_ezsignfoldertype_id = 5, 
                        fki_language_id = 2, 
                        s_ezsigntemplatepackage_description = 'Package for new clients', 
                        b_ezsigntemplatepackage_needvalidation = True, 
                        i_ezsigntemplatepackagemembership = 56, 
                        s_ezsignfoldertype_name_x = 'Default', 
                        b_ezsigntemplatepackage_isactive = True, )
                    ]
            )
        else:
            return EzsigntemplatepackageGetListV1ResponseMPayload(
                a_obj_ezsigntemplatepackage = [
                    eZmaxApi.models.ezsigntemplatepackage_list_element.ezsigntemplatepackage-ListElement(
                        pki_ezsigntemplatepackage_id = 99, 
                        fki_ezsignfoldertype_id = 5, 
                        fki_language_id = 2, 
                        s_ezsigntemplatepackage_description = 'Package for new clients', 
                        b_ezsigntemplatepackage_needvalidation = True, 
                        i_ezsigntemplatepackagemembership = 56, 
                        s_ezsignfoldertype_name_x = 'Default', 
                        b_ezsigntemplatepackage_isactive = True, )
                    ],
        )
        """

    def testEzsigntemplatepackageGetListV1ResponseMPayload(self):
        """Test EzsigntemplatepackageGetListV1ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
