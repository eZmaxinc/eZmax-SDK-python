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

from eZmaxApi.models.ezsignsignergroup_request import EzsignsignergroupRequest

class TestEzsignsignergroupRequest(unittest.TestCase):
    """EzsignsignergroupRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsignsignergroupRequest:
        """Test EzsignsignergroupRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsignsignergroupRequest`
        """
        model = EzsignsignergroupRequest()
        if include_optional:
            return EzsignsignergroupRequest(
                pki_ezsignsignergroup_id = 27,
                fki_ezsignfolder_id = 33,
                obj_ezsignsignergroup_description = eZmaxApi.models.multilingual_ezsignsignergroup_description.Multilingual-EzsignsignergroupDescription(
                    s_ezsignsignergroup_description1 = 'RH', 
                    s_ezsignsignergroup_description2 = 'HR', )
            )
        else:
            return EzsignsignergroupRequest(
                fki_ezsignfolder_id = 33,
                obj_ezsignsignergroup_description = eZmaxApi.models.multilingual_ezsignsignergroup_description.Multilingual-EzsignsignergroupDescription(
                    s_ezsignsignergroup_description1 = 'RH', 
                    s_ezsignsignergroup_description2 = 'HR', ),
        )
        """

    def testEzsignsignergroupRequest(self):
        """Test EzsignsignergroupRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
