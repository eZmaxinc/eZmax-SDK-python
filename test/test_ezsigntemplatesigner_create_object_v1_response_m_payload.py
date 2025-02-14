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

from eZmaxApi.models.ezsigntemplatesigner_create_object_v1_response_m_payload import EzsigntemplatesignerCreateObjectV1ResponseMPayload

class TestEzsigntemplatesignerCreateObjectV1ResponseMPayload(unittest.TestCase):
    """EzsigntemplatesignerCreateObjectV1ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsigntemplatesignerCreateObjectV1ResponseMPayload:
        """Test EzsigntemplatesignerCreateObjectV1ResponseMPayload
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsigntemplatesignerCreateObjectV1ResponseMPayload`
        """
        model = EzsigntemplatesignerCreateObjectV1ResponseMPayload()
        if include_optional:
            return EzsigntemplatesignerCreateObjectV1ResponseMPayload(
                a_pki_ezsigntemplatesigner_id = [
                    9
                    ],
                b_ezsigntemplatepackage_needvalidation = True,
                b_ezsignbulksend_needvalidation = True
            )
        else:
            return EzsigntemplatesignerCreateObjectV1ResponseMPayload(
                a_pki_ezsigntemplatesigner_id = [
                    9
                    ],
                b_ezsigntemplatepackage_needvalidation = True,
                b_ezsignbulksend_needvalidation = True,
        )
        """

    def testEzsigntemplatesignerCreateObjectV1ResponseMPayload(self):
        """Test EzsigntemplatesignerCreateObjectV1ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
