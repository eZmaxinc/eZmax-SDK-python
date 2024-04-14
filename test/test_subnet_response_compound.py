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

from eZmaxApi.models.subnet_response_compound import SubnetResponseCompound

class TestSubnetResponseCompound(unittest.TestCase):
    """SubnetResponseCompound unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SubnetResponseCompound:
        """Test SubnetResponseCompound
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SubnetResponseCompound`
        """
        model = SubnetResponseCompound()
        if include_optional:
            return SubnetResponseCompound(
                pki_subnet_id = 3,
                fki_user_id = 70,
                fki_apikey_id = 99,
                obj_subnet_description = eZmaxApi.models.multilingual_subnet_description.Multilingual-SubnetDescription(
                    s_subnet_description1 = 'Bureau chef', 
                    s_subnet_description2 = 'Head office', ),
                i_subnet_network = 134744064,
                i_subnet_mask = 4294967040
            )
        else:
            return SubnetResponseCompound(
                pki_subnet_id = 3,
                obj_subnet_description = eZmaxApi.models.multilingual_subnet_description.Multilingual-SubnetDescription(
                    s_subnet_description1 = 'Bureau chef', 
                    s_subnet_description2 = 'Head office', ),
                i_subnet_network = 134744064,
                i_subnet_mask = 4294967040,
        )
        """

    def testSubnetResponseCompound(self):
        """Test SubnetResponseCompound"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
