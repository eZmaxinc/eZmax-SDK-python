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

from eZmaxApi.models.ezsignfoldersignerassociation_get_object_v2_response import EzsignfoldersignerassociationGetObjectV2Response

class TestEzsignfoldersignerassociationGetObjectV2Response(unittest.TestCase):
    """EzsignfoldersignerassociationGetObjectV2Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsignfoldersignerassociationGetObjectV2Response:
        """Test EzsignfoldersignerassociationGetObjectV2Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsignfoldersignerassociationGetObjectV2Response`
        """
        model = EzsignfoldersignerassociationGetObjectV2Response()
        if include_optional:
            return EzsignfoldersignerassociationGetObjectV2Response(
                m_payload = eZmaxApi.models.ezsignfoldersignerassociation_get_object_v2_response_m_payload.ezsignfoldersignerassociation-getObject-v2-Response-mPayload(
                    obj_ezsignfoldersignerassociation = eZmaxApi.models.ezsignfoldersignerassociation_response_compound.ezsignfoldersignerassociation-ResponseCompound(), )
            )
        else:
            return EzsignfoldersignerassociationGetObjectV2Response(
                m_payload = eZmaxApi.models.ezsignfoldersignerassociation_get_object_v2_response_m_payload.ezsignfoldersignerassociation-getObject-v2-Response-mPayload(
                    obj_ezsignfoldersignerassociation = eZmaxApi.models.ezsignfoldersignerassociation_response_compound.ezsignfoldersignerassociation-ResponseCompound(), ),
        )
        """

    def testEzsignfoldersignerassociationGetObjectV2Response(self):
        """Test EzsignfoldersignerassociationGetObjectV2Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
