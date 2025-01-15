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

from eZmaxApi.models.ezdoctemplatedocument_request_patch import EzdoctemplatedocumentRequestPatch

class TestEzdoctemplatedocumentRequestPatch(unittest.TestCase):
    """EzdoctemplatedocumentRequestPatch unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzdoctemplatedocumentRequestPatch:
        """Test EzdoctemplatedocumentRequestPatch
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzdoctemplatedocumentRequestPatch`
        """
        model = EzdoctemplatedocumentRequestPatch()
        if include_optional:
            return EzdoctemplatedocumentRequestPatch(
                e_ezdoctemplatedocument_format = 'Docx',
                s_ezdoctemplatedocument_fields = 'jUR,rZ#UM/?R,Fp^l6$ARj',
                s_ezdoctemplatedocument_base64 = '[B@782a4fff'
            )
        else:
            return EzdoctemplatedocumentRequestPatch(
        )
        """

    def testEzdoctemplatedocumentRequestPatch(self):
        """Test EzdoctemplatedocumentRequestPatch"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
