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

from eZmaxApi.models.ezsigndiscussion_request_compound import EzsigndiscussionRequestCompound

class TestEzsigndiscussionRequestCompound(unittest.TestCase):
    """EzsigndiscussionRequestCompound unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsigndiscussionRequestCompound:
        """Test EzsigndiscussionRequestCompound
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsigndiscussionRequestCompound`
        """
        model = EzsigndiscussionRequestCompound()
        if include_optional:
            return EzsigndiscussionRequestCompound(
                pki_ezsigndiscussion_id = 194,
                fki_ezsigndocument_id = 97,
                i_ezsigndiscussion_pagenumber = 4,
                i_ezsigndiscussion_x = 57208,
                i_ezsigndiscussion_y = 57652,
                obj_discussion = eZmaxApi.models.discussion_request.discussion-Request(
                    pki_discussion_id = 125, 
                    s_discussion_description = 'John Doe', 
                    b_discussion_closed = True, )
            )
        else:
            return EzsigndiscussionRequestCompound(
                fki_ezsigndocument_id = 97,
                i_ezsigndiscussion_pagenumber = 4,
                i_ezsigndiscussion_x = 57208,
                i_ezsigndiscussion_y = 57652,
                obj_discussion = eZmaxApi.models.discussion_request.discussion-Request(
                    pki_discussion_id = 125, 
                    s_discussion_description = 'John Doe', 
                    b_discussion_closed = True, ),
        )
        """

    def testEzsigndiscussionRequestCompound(self):
        """Test EzsigndiscussionRequestCompound"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
