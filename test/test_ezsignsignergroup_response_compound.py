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

from eZmaxApi.models.ezsignsignergroup_response_compound import EzsignsignergroupResponseCompound

class TestEzsignsignergroupResponseCompound(unittest.TestCase):
    """EzsignsignergroupResponseCompound unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsignsignergroupResponseCompound:
        """Test EzsignsignergroupResponseCompound
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsignsignergroupResponseCompound`
        """
        model = EzsignsignergroupResponseCompound()
        if include_optional:
            return EzsignsignergroupResponseCompound(
                pki_ezsignsignergroup_id = 27,
                obj_ezsignsignergroup_description = eZmaxApi.models.multilingual_ezsignsignergroup_description.Multilingual-EzsignsignergroupDescription(
                    s_ezsignsignergroup_description1 = 'RH', 
                    s_ezsignsignergroup_description2 = 'HR', ),
                s_ezsignsignergroup_description_x = 'HR'
            )
        else:
            return EzsignsignergroupResponseCompound(
                pki_ezsignsignergroup_id = 27,
                obj_ezsignsignergroup_description = eZmaxApi.models.multilingual_ezsignsignergroup_description.Multilingual-EzsignsignergroupDescription(
                    s_ezsignsignergroup_description1 = 'RH', 
                    s_ezsignsignergroup_description2 = 'HR', ),
        )
        """

    def testEzsignsignergroupResponseCompound(self):
        """Test EzsignsignergroupResponseCompound"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
