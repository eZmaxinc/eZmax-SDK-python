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

from eZmaxApi.models.apikey_request_compound import ApikeyRequestCompound

class TestApikeyRequestCompound(unittest.TestCase):
    """ApikeyRequestCompound unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApikeyRequestCompound:
        """Test ApikeyRequestCompound
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApikeyRequestCompound`
        """
        model = ApikeyRequestCompound()
        if include_optional:
            return ApikeyRequestCompound(
                pki_apikey_id = 99,
                fki_user_id = 70,
                obj_apikey_description = eZmaxApi.models.multilingual_apikey_description.Multilingual-ApikeyDescription(
                    s_apikey_description1 = 'Projet X', 
                    s_apikey_description2 = 'Project X', ),
                b_apikey_isactive = True,
                b_apikey_issigned = True
            )
        else:
            return ApikeyRequestCompound(
                fki_user_id = 70,
                obj_apikey_description = eZmaxApi.models.multilingual_apikey_description.Multilingual-ApikeyDescription(
                    s_apikey_description1 = 'Projet X', 
                    s_apikey_description2 = 'Project X', ),
        )
        """

    def testApikeyRequestCompound(self):
        """Test ApikeyRequestCompound"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
