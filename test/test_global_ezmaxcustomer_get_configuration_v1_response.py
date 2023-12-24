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

from eZmaxApi.models.global_ezmaxcustomer_get_configuration_v1_response import GlobalEzmaxcustomerGetConfigurationV1Response

class TestGlobalEzmaxcustomerGetConfigurationV1Response(unittest.TestCase):
    """GlobalEzmaxcustomerGetConfigurationV1Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GlobalEzmaxcustomerGetConfigurationV1Response:
        """Test GlobalEzmaxcustomerGetConfigurationV1Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GlobalEzmaxcustomerGetConfigurationV1Response`
        """
        model = GlobalEzmaxcustomerGetConfigurationV1Response()
        if include_optional:
            return GlobalEzmaxcustomerGetConfigurationV1Response(
                s_infrastructureregion_code = 'ca-central-1',
                s_infrastructureregion_code_web = 'ca-central-1',
                s_infrastructureenvironmenttype_description = 'prod',
                s_cognito_client_id_external = '6kivk421lhteuktijfsvv4r1cl',
                s_cognito_client_id_ezmaxpublic = '6kivk421lhteuktijfsvv4r1cl'
            )
        else:
            return GlobalEzmaxcustomerGetConfigurationV1Response(
                s_infrastructureregion_code = 'ca-central-1',
                s_infrastructureregion_code_web = 'ca-central-1',
                s_infrastructureenvironmenttype_description = 'prod',
                s_cognito_client_id_ezmaxpublic = '6kivk421lhteuktijfsvv4r1cl',
        )
        """

    def testGlobalEzmaxcustomerGetConfigurationV1Response(self):
        """Test GlobalEzmaxcustomerGetConfigurationV1Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
