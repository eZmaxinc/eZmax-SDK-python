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

from eZmaxApi.models.ezdoctemplatedocument_edit_object_v1_request import EzdoctemplatedocumentEditObjectV1Request

class TestEzdoctemplatedocumentEditObjectV1Request(unittest.TestCase):
    """EzdoctemplatedocumentEditObjectV1Request unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzdoctemplatedocumentEditObjectV1Request:
        """Test EzdoctemplatedocumentEditObjectV1Request
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzdoctemplatedocumentEditObjectV1Request`
        """
        model = EzdoctemplatedocumentEditObjectV1Request()
        if include_optional:
            return EzdoctemplatedocumentEditObjectV1Request(
                obj_ezdoctemplatedocument = eZmaxApi.models.ezdoctemplatedocument_request_compound.ezdoctemplatedocument-RequestCompound()
            )
        else:
            return EzdoctemplatedocumentEditObjectV1Request(
                obj_ezdoctemplatedocument = eZmaxApi.models.ezdoctemplatedocument_request_compound.ezdoctemplatedocument-RequestCompound(),
        )
        """

    def testEzdoctemplatedocumentEditObjectV1Request(self):
        """Test EzdoctemplatedocumentEditObjectV1Request"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
