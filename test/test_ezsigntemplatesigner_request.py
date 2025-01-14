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

from eZmaxApi.models.ezsigntemplatesigner_request import EzsigntemplatesignerRequest

class TestEzsigntemplatesignerRequest(unittest.TestCase):
    """EzsigntemplatesignerRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsigntemplatesignerRequest:
        """Test EzsigntemplatesignerRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsigntemplatesignerRequest`
        """
        model = EzsigntemplatesignerRequest()
        if include_optional:
            return EzsigntemplatesignerRequest(
                pki_ezsigntemplatesigner_id = 9,
                fki_ezsigntemplate_id = 36,
                fki_user_id = 70,
                fki_usergroup_id = 2,
                fki_ezdoctemplatedocument_id = 95,
                b_ezsigntemplatesigner_receivecopy = True,
                e_ezsigntemplatesigner_mapping = 'Manual',
                s_ezsigntemplatesigner_description = 'Customer'
            )
        else:
            return EzsigntemplatesignerRequest(
                fki_ezsigntemplate_id = 36,
                s_ezsigntemplatesigner_description = 'Customer',
        )
        """

    def testEzsigntemplatesignerRequest(self):
        """Test EzsigntemplatesignerRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
