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

from eZmaxApi.models.ezsigntemplatepackagesignermembership_delete_object_v1_response_m_payload import EzsigntemplatepackagesignermembershipDeleteObjectV1ResponseMPayload

class TestEzsigntemplatepackagesignermembershipDeleteObjectV1ResponseMPayload(unittest.TestCase):
    """EzsigntemplatepackagesignermembershipDeleteObjectV1ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsigntemplatepackagesignermembershipDeleteObjectV1ResponseMPayload:
        """Test EzsigntemplatepackagesignermembershipDeleteObjectV1ResponseMPayload
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsigntemplatepackagesignermembershipDeleteObjectV1ResponseMPayload`
        """
        model = EzsigntemplatepackagesignermembershipDeleteObjectV1ResponseMPayload()
        if include_optional:
            return EzsigntemplatepackagesignermembershipDeleteObjectV1ResponseMPayload(
                b_ezsigntemplatepackage_needvalidation = True,
                b_ezsignbulksend_needvalidation = True
            )
        else:
            return EzsigntemplatepackagesignermembershipDeleteObjectV1ResponseMPayload(
                b_ezsigntemplatepackage_needvalidation = True,
                b_ezsignbulksend_needvalidation = True,
        )
        """

    def testEzsigntemplatepackagesignermembershipDeleteObjectV1ResponseMPayload(self):
        """Test EzsigntemplatepackagesignermembershipDeleteObjectV1ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
