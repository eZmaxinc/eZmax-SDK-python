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

from eZmaxApi.models.ezsignsignature_get_ezsignsignatureattachment_v1_response_m_payload import EzsignsignatureGetEzsignsignatureattachmentV1ResponseMPayload

class TestEzsignsignatureGetEzsignsignatureattachmentV1ResponseMPayload(unittest.TestCase):
    """EzsignsignatureGetEzsignsignatureattachmentV1ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsignsignatureGetEzsignsignatureattachmentV1ResponseMPayload:
        """Test EzsignsignatureGetEzsignsignatureattachmentV1ResponseMPayload
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsignsignatureGetEzsignsignatureattachmentV1ResponseMPayload`
        """
        model = EzsignsignatureGetEzsignsignatureattachmentV1ResponseMPayload()
        if include_optional:
            return EzsignsignatureGetEzsignsignatureattachmentV1ResponseMPayload(
                a_obj_ezsignsignatureattachment = [
                    eZmaxApi.models.ezsignsignatureattachment_response.ezsignsignatureattachment-Response(
                        pki_ezsignsignatureattachment_id = 177, 
                        fki_ezsignsignature_id = 49, 
                        bin_ezsignsignatureattachment_md5 = '098f6bcd4621d373cade4e832627b4f6', 
                        s_ezsignsignatureattachment_name = 'document.pdf', 
                        s_download_url = 'http://www.example.com/document.pdf', )
                    ]
            )
        else:
            return EzsignsignatureGetEzsignsignatureattachmentV1ResponseMPayload(
                a_obj_ezsignsignatureattachment = [
                    eZmaxApi.models.ezsignsignatureattachment_response.ezsignsignatureattachment-Response(
                        pki_ezsignsignatureattachment_id = 177, 
                        fki_ezsignsignature_id = 49, 
                        bin_ezsignsignatureattachment_md5 = '098f6bcd4621d373cade4e832627b4f6', 
                        s_ezsignsignatureattachment_name = 'document.pdf', 
                        s_download_url = 'http://www.example.com/document.pdf', )
                    ],
        )
        """

    def testEzsignsignatureGetEzsignsignatureattachmentV1ResponseMPayload(self):
        """Test EzsignsignatureGetEzsignsignatureattachmentV1ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
