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

from eZmaxApi.models.systemconfiguration_response_compound import SystemconfigurationResponseCompound  # noqa: E501

class TestSystemconfigurationResponseCompound(unittest.TestCase):
    """SystemconfigurationResponseCompound unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SystemconfigurationResponseCompound:
        """Test SystemconfigurationResponseCompound
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SystemconfigurationResponseCompound`
        """
        model = SystemconfigurationResponseCompound()  # noqa: E501
        if include_optional:
            return SystemconfigurationResponseCompound(
                pki_systemconfiguration_id = 1,
                fki_systemconfigurationtype_id = 28,
                s_systemconfigurationtype_description_x = 'eZsign (Pro)',
                e_systemconfiguration_newexternaluseraction = 'Stage',
                e_systemconfiguration_language1 = 'fr_QC',
                e_systemconfiguration_language2 = 'en_CA',
                e_systemconfiguration_ezsign = 'Yes',
                b_systemconfiguration_ezsignpersonnal = True,
                b_systemconfiguration_sspr = True,
                dt_systemconfiguration_readonlyexpirationstart = '2020-12-31',
                dt_systemconfiguration_readonlyexpirationend = '2021-12-31'
            )
        else:
            return SystemconfigurationResponseCompound(
                pki_systemconfiguration_id = 1,
                fki_systemconfigurationtype_id = 28,
                s_systemconfigurationtype_description_x = 'eZsign (Pro)',
                e_systemconfiguration_newexternaluseraction = 'Stage',
                e_systemconfiguration_language1 = 'fr_QC',
                e_systemconfiguration_language2 = 'en_CA',
                e_systemconfiguration_ezsign = 'Yes',
                b_systemconfiguration_ezsignpersonnal = True,
                b_systemconfiguration_sspr = True,
        )
        """

    def testSystemconfigurationResponseCompound(self):
        """Test SystemconfigurationResponseCompound"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
