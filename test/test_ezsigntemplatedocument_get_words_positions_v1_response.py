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

from eZmaxApi.models.ezsigntemplatedocument_get_words_positions_v1_response import EzsigntemplatedocumentGetWordsPositionsV1Response

class TestEzsigntemplatedocumentGetWordsPositionsV1Response(unittest.TestCase):
    """EzsigntemplatedocumentGetWordsPositionsV1Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsigntemplatedocumentGetWordsPositionsV1Response:
        """Test EzsigntemplatedocumentGetWordsPositionsV1Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsigntemplatedocumentGetWordsPositionsV1Response`
        """
        model = EzsigntemplatedocumentGetWordsPositionsV1Response()
        if include_optional:
            return EzsigntemplatedocumentGetWordsPositionsV1Response(
                obj_debug_payload = eZmaxApi.models.common_response_obj_debug_payload.Common-Response-objDebugPayload(
                    i_version_min = 1, 
                    i_version_max = 2, 
                    a_required_permission = [
                        117
                        ], 
                    b_version_deprecated = False, 
                    dt_response_date = '2020-12-31 23:59:59', ),
                obj_debug = {"sMemoryUsage":"11,923MB","sRunTime":"0.6084s","iSQLSelects":3,"iSQLQueries":6,"a_objSQLQuery":[{"sQuery":"SELECT * FROM table","fDuration":1.0E-4},{"sQuery":"SELECT * FROM table","fDuration":1.0E-4}]},
                m_payload = [
                    eZmaxApi.models.custom_word_position_word_response.Custom-WordPositionWord-Response(
                        s_word = '', 
                        a_obj_word_position_occurence = [
                            eZmaxApi.models.custom_word_position_occurence_response.Custom-WordPositionOccurence-Response(
                                i_page = 1, 
                                i_x = 0, 
                                i_y = 0, )
                            ], )
                    ]
            )
        else:
            return EzsigntemplatedocumentGetWordsPositionsV1Response(
                obj_debug_payload = eZmaxApi.models.common_response_obj_debug_payload.Common-Response-objDebugPayload(
                    i_version_min = 1, 
                    i_version_max = 2, 
                    a_required_permission = [
                        117
                        ], 
                    b_version_deprecated = False, 
                    dt_response_date = '2020-12-31 23:59:59', ),
                m_payload = [
                    eZmaxApi.models.custom_word_position_word_response.Custom-WordPositionWord-Response(
                        s_word = '', 
                        a_obj_word_position_occurence = [
                            eZmaxApi.models.custom_word_position_occurence_response.Custom-WordPositionOccurence-Response(
                                i_page = 1, 
                                i_x = 0, 
                                i_y = 0, )
                            ], )
                    ],
        )
        """

    def testEzsigntemplatedocumentGetWordsPositionsV1Response(self):
        """Test EzsigntemplatedocumentGetWordsPositionsV1Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
