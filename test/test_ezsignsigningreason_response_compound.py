# coding: utf-8

"""
    eZmax API Definition (Full)

    This API expose all the functionnalities for the eZmax and eZsign applications.

    The version of the OpenAPI document: 1.2.0
    Contact: support-api@ezmax.ca
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from eZmaxApi.models.ezsignsigningreason_response_compound import EzsignsigningreasonResponseCompound

class TestEzsignsigningreasonResponseCompound(unittest.TestCase):
    """EzsignsigningreasonResponseCompound unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsignsigningreasonResponseCompound:
        """Test EzsignsigningreasonResponseCompound
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsignsigningreasonResponseCompound`
        """
        model = EzsignsigningreasonResponseCompound()
        if include_optional:
            return EzsignsigningreasonResponseCompound(
                pki_ezsignsigningreason_id = 194,
                obj_ezsignsigningreason_description = eZmaxApi.models.multilingual_ezsignsigningreason_description.Multilingual-EzsignsigningreasonDescription(
                    s_ezsignsigningreason_description1 = 'J'approuve ce document', 
                    s_ezsignsigningreason_description2 = 'I approve this document', ),
                b_ezsignsigningreason_isactive = True
            )
        else:
            return EzsignsigningreasonResponseCompound(
                pki_ezsignsigningreason_id = 194,
                obj_ezsignsigningreason_description = eZmaxApi.models.multilingual_ezsignsigningreason_description.Multilingual-EzsignsigningreasonDescription(
                    s_ezsignsigningreason_description1 = 'J'approuve ce document', 
                    s_ezsignsigningreason_description2 = 'I approve this document', ),
                b_ezsignsigningreason_isactive = True,
        )
        """

    def testEzsignsigningreasonResponseCompound(self):
        """Test EzsignsigningreasonResponseCompound"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
