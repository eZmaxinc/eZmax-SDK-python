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

from eZmaxApi.models.custom_ezsignfoldertransmission_signer_response import CustomEzsignfoldertransmissionSignerResponse

class TestCustomEzsignfoldertransmissionSignerResponse(unittest.TestCase):
    """CustomEzsignfoldertransmissionSignerResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CustomEzsignfoldertransmissionSignerResponse:
        """Test CustomEzsignfoldertransmissionSignerResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CustomEzsignfoldertransmissionSignerResponse`
        """
        model = CustomEzsignfoldertransmissionSignerResponse()
        if include_optional:
            return CustomEzsignfoldertransmissionSignerResponse(
                fki_user_id = 70,
                s_contact_firstname = 'John',
                s_contact_lastname = 'Doe'
            )
        else:
            return CustomEzsignfoldertransmissionSignerResponse(
                s_contact_firstname = 'John',
                s_contact_lastname = 'Doe',
        )
        """

    def testCustomEzsignfoldertransmissionSignerResponse(self):
        """Test CustomEzsignfoldertransmissionSignerResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
