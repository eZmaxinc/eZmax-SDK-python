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

from eZmaxApi.models.ezsigntemplatepublic_get_ezsigntemplatepublic_details_v1_response import EzsigntemplatepublicGetEzsigntemplatepublicDetailsV1Response

class TestEzsigntemplatepublicGetEzsigntemplatepublicDetailsV1Response(unittest.TestCase):
    """EzsigntemplatepublicGetEzsigntemplatepublicDetailsV1Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsigntemplatepublicGetEzsigntemplatepublicDetailsV1Response:
        """Test EzsigntemplatepublicGetEzsigntemplatepublicDetailsV1Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsigntemplatepublicGetEzsigntemplatepublicDetailsV1Response`
        """
        model = EzsigntemplatepublicGetEzsigntemplatepublicDetailsV1Response()
        if include_optional:
            return EzsigntemplatepublicGetEzsigntemplatepublicDetailsV1Response(
                m_payload = eZmaxApi.models.ezsigntemplatepublic_get_ezsigntemplatepublic_details_v1_response_m_payload.ezsigntemplatepublic-getEzsigntemplatepublicDetails-v1-Response-mPayload(
                    obj_branding = eZmaxApi.models.custom_branding_response.Custom-Branding-Response(
                        i_branding_color = 15658734, 
                        s_branding_logointerfaceurl = 'http://www.example.com/logo.jpg', ), 
                    fki_userlogintype_id = 2, 
                    a_s_ezsigntemplatesigner_description = [
                        'http://www.website.com/avatar.jpg'
                        ], )
            )
        else:
            return EzsigntemplatepublicGetEzsigntemplatepublicDetailsV1Response(
                m_payload = eZmaxApi.models.ezsigntemplatepublic_get_ezsigntemplatepublic_details_v1_response_m_payload.ezsigntemplatepublic-getEzsigntemplatepublicDetails-v1-Response-mPayload(
                    obj_branding = eZmaxApi.models.custom_branding_response.Custom-Branding-Response(
                        i_branding_color = 15658734, 
                        s_branding_logointerfaceurl = 'http://www.example.com/logo.jpg', ), 
                    fki_userlogintype_id = 2, 
                    a_s_ezsigntemplatesigner_description = [
                        'http://www.website.com/avatar.jpg'
                        ], ),
        )
        """

    def testEzsigntemplatepublicGetEzsigntemplatepublicDetailsV1Response(self):
        """Test EzsigntemplatepublicGetEzsigntemplatepublicDetailsV1Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
