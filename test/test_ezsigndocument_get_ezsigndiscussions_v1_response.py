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

from eZmaxApi.models.ezsigndocument_get_ezsigndiscussions_v1_response import EzsigndocumentGetEzsigndiscussionsV1Response

class TestEzsigndocumentGetEzsigndiscussionsV1Response(unittest.TestCase):
    """EzsigndocumentGetEzsigndiscussionsV1Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsigndocumentGetEzsigndiscussionsV1Response:
        """Test EzsigndocumentGetEzsigndiscussionsV1Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsigndocumentGetEzsigndiscussionsV1Response`
        """
        model = EzsigndocumentGetEzsigndiscussionsV1Response()
        if include_optional:
            return EzsigndocumentGetEzsigndiscussionsV1Response(
                m_payload = eZmaxApi.models.ezsigndocument_get_ezsigndiscussions_v1_response_m_payload.ezsigndocument-getEzsigndiscussions-v1-Response-mPayload(
                    a_obj_ezsigndiscussion = [
                        eZmaxApi.models.ezsigndiscussion_response.ezsigndiscussion-Response(
                            pki_ezsigndiscussion_id = 194, 
                            fki_ezsignpage_id = 64, 
                            fki_discussion_id = 125, 
                            i_ezsigndiscussion_x = 57208, 
                            i_ezsigndiscussion_y = 57652, 
                            i_ezsigndiscussion_pagenumber = 4, 
                            obj_discussion = eZmaxApi.models.discussion_response_compound.discussion-ResponseCompound(), )
                        ], )
            )
        else:
            return EzsigndocumentGetEzsigndiscussionsV1Response(
                m_payload = eZmaxApi.models.ezsigndocument_get_ezsigndiscussions_v1_response_m_payload.ezsigndocument-getEzsigndiscussions-v1-Response-mPayload(
                    a_obj_ezsigndiscussion = [
                        eZmaxApi.models.ezsigndiscussion_response.ezsigndiscussion-Response(
                            pki_ezsigndiscussion_id = 194, 
                            fki_ezsignpage_id = 64, 
                            fki_discussion_id = 125, 
                            i_ezsigndiscussion_x = 57208, 
                            i_ezsigndiscussion_y = 57652, 
                            i_ezsigndiscussion_pagenumber = 4, 
                            obj_discussion = eZmaxApi.models.discussion_response_compound.discussion-ResponseCompound(), )
                        ], ),
        )
        """

    def testEzsigndocumentGetEzsigndiscussionsV1Response(self):
        """Test EzsigndocumentGetEzsigndiscussionsV1Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
