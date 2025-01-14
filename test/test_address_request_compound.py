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

from eZmaxApi.models.address_request_compound import AddressRequestCompound

class TestAddressRequestCompound(unittest.TestCase):
    """AddressRequestCompound unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AddressRequestCompound:
        """Test AddressRequestCompound
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AddressRequestCompound`
        """
        model = AddressRequestCompound()
        if include_optional:
            return AddressRequestCompound(
                pki_address_id = 142,
                fki_addresstype_id = 1,
                s_address_civic = '2540',
                s_address_street = 'Daniel-Johnson Blvd.',
                s_address_suite = '610',
                s_address_city = 'Laval',
                fki_province_id = 11,
                fki_country_id = 1,
                s_address_zip = 'H7T2S3',
                f_address_longitude = 'doej',
                f_address_latitude = 'doej'
            )
        else:
            return AddressRequestCompound(
                fki_addresstype_id = 1,
                s_address_civic = '2540',
                s_address_street = 'Daniel-Johnson Blvd.',
                s_address_city = 'Laval',
                fki_province_id = 11,
                fki_country_id = 1,
                s_address_zip = 'H7T2S3',
        )
        """

    def testAddressRequestCompound(self):
        """Test AddressRequestCompound"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
