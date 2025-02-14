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

from eZmaxApi.models.ezsigndocument_create_object_v3_response_m_payload import EzsigndocumentCreateObjectV3ResponseMPayload

class TestEzsigndocumentCreateObjectV3ResponseMPayload(unittest.TestCase):
    """EzsigndocumentCreateObjectV3ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsigndocumentCreateObjectV3ResponseMPayload:
        """Test EzsigndocumentCreateObjectV3ResponseMPayload
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsigndocumentCreateObjectV3ResponseMPayload`
        """
        model = EzsigndocumentCreateObjectV3ResponseMPayload()
        if include_optional:
            return EzsigndocumentCreateObjectV3ResponseMPayload(
                a_obj_ezsigndocument = [
                    eZmaxApi.models.ezsigndocument_create_element_v3_response.ezsigndocument-createElement-v3-Response(
                        pki_ezsigndocument_id = 97, 
                        a_obj_matchingtemplate = [
                            eZmaxApi.models.ezsigndocument_matchingtemplate_v3_response.ezsigndocument-matchingtemplate-v3-Response(
                                pki_ezsigntemplate_id = 36, 
                                pki_ezsigntemplateglobal_id = 36, )
                            ], )
                    ]
            )
        else:
            return EzsigndocumentCreateObjectV3ResponseMPayload(
                a_obj_ezsigndocument = [
                    eZmaxApi.models.ezsigndocument_create_element_v3_response.ezsigndocument-createElement-v3-Response(
                        pki_ezsigndocument_id = 97, 
                        a_obj_matchingtemplate = [
                            eZmaxApi.models.ezsigndocument_matchingtemplate_v3_response.ezsigndocument-matchingtemplate-v3-Response(
                                pki_ezsigntemplate_id = 36, 
                                pki_ezsigntemplateglobal_id = 36, )
                            ], )
                    ],
        )
        """

    def testEzsigndocumentCreateObjectV3ResponseMPayload(self):
        """Test EzsigndocumentCreateObjectV3ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
