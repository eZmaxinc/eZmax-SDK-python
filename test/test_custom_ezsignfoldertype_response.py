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

from eZmaxApi.models.custom_ezsignfoldertype_response import CustomEzsignfoldertypeResponse

class TestCustomEzsignfoldertypeResponse(unittest.TestCase):
    """CustomEzsignfoldertypeResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CustomEzsignfoldertypeResponse:
        """Test CustomEzsignfoldertypeResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CustomEzsignfoldertypeResponse`
        """
        model = CustomEzsignfoldertypeResponse()
        if include_optional:
            return CustomEzsignfoldertypeResponse(
                pki_ezsignfoldertype_id = 5,
                s_ezsignfoldertype_name_x = 'Default',
                b_ezsignfoldertype_sendproofezsignsigner = False,
                b_ezsignfoldertype_allowdownloadattachmentezsignsigner = False,
                b_ezsignfoldertype_allowdownloadproofezsignsigner = False,
                b_ezsignfoldertype_delegate = True,
                b_ezsignfoldertype_discussion = True,
                b_ezsignfoldertype_reassignezsignsigner = True,
                b_ezsignfoldertype_reassignuser = True
            )
        else:
            return CustomEzsignfoldertypeResponse(
                pki_ezsignfoldertype_id = 5,
        )
        """

    def testCustomEzsignfoldertypeResponse(self):
        """Test CustomEzsignfoldertypeResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
