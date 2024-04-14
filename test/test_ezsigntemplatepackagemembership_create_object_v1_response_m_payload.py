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

from eZmaxApi.models.ezsigntemplatepackagemembership_create_object_v1_response_m_payload import EzsigntemplatepackagemembershipCreateObjectV1ResponseMPayload

class TestEzsigntemplatepackagemembershipCreateObjectV1ResponseMPayload(unittest.TestCase):
    """EzsigntemplatepackagemembershipCreateObjectV1ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsigntemplatepackagemembershipCreateObjectV1ResponseMPayload:
        """Test EzsigntemplatepackagemembershipCreateObjectV1ResponseMPayload
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsigntemplatepackagemembershipCreateObjectV1ResponseMPayload`
        """
        model = EzsigntemplatepackagemembershipCreateObjectV1ResponseMPayload()
        if include_optional:
            return EzsigntemplatepackagemembershipCreateObjectV1ResponseMPayload(
                a_pki_ezsigntemplatepackagemembership_id = [
                    194
                    ],
                b_ezsigntemplatepackage_needvalidation = True,
                b_ezsignbulksend_needvalidation = True
            )
        else:
            return EzsigntemplatepackagemembershipCreateObjectV1ResponseMPayload(
                a_pki_ezsigntemplatepackagemembership_id = [
                    194
                    ],
                b_ezsigntemplatepackage_needvalidation = True,
                b_ezsignbulksend_needvalidation = True,
        )
        """

    def testEzsigntemplatepackagemembershipCreateObjectV1ResponseMPayload(self):
        """Test EzsigntemplatepackagemembershipCreateObjectV1ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
