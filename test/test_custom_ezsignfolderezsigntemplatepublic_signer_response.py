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

from eZmaxApi.models.custom_ezsignfolderezsigntemplatepublic_signer_response import CustomEzsignfolderezsigntemplatepublicSignerResponse

class TestCustomEzsignfolderezsigntemplatepublicSignerResponse(unittest.TestCase):
    """CustomEzsignfolderezsigntemplatepublicSignerResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CustomEzsignfolderezsigntemplatepublicSignerResponse:
        """Test CustomEzsignfolderezsigntemplatepublicSignerResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CustomEzsignfolderezsigntemplatepublicSignerResponse`
        """
        model = CustomEzsignfolderezsigntemplatepublicSignerResponse()
        if include_optional:
            return CustomEzsignfolderezsigntemplatepublicSignerResponse(
                fki_user_id = 70,
                fki_ezsignsignergroup_id = 27,
                s_contact_firstname = 'John',
                s_contact_lastname = 'Doe',
                s_ezsignsignergroup_description_x = 'HR'
            )
        else:
            return CustomEzsignfolderezsigntemplatepublicSignerResponse(
        )
        """

    def testCustomEzsignfolderezsigntemplatepublicSignerResponse(self):
        """Test CustomEzsignfolderezsigntemplatepublicSignerResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
