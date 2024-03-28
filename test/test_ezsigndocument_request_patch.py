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

from eZmaxApi.models.ezsigndocument_request_patch import EzsigndocumentRequestPatch

class TestEzsigndocumentRequestPatch(unittest.TestCase):
    """EzsigndocumentRequestPatch unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsigndocumentRequestPatch:
        """Test EzsigndocumentRequestPatch
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsigndocumentRequestPatch`
        """
        model = EzsigndocumentRequestPatch()
        if include_optional:
            return EzsigndocumentRequestPatch(
                dt_ezsigndocument_duedate = '2020-12-31 23:59:59',
                s_ezsigndocument_name = 'Contract #123'
            )
        else:
            return EzsigndocumentRequestPatch(
        )
        """

    def testEzsigndocumentRequestPatch(self):
        """Test EzsigndocumentRequestPatch"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
