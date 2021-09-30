"""
    eZmax API Definition

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.1.0
    Contact: support-api@ezmax.ca
    Generated by: https://openapi-generator.tech
"""


import unittest

import eZmaxApi
from eZmaxApi.api.object_ezsignsignature_api import ObjectEzsignsignatureApi  # noqa: E501


class TestObjectEzsignsignatureApi(unittest.TestCase):
    """ObjectEzsignsignatureApi unit test stubs"""

    def setUp(self):
        self.api = ObjectEzsignsignatureApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_ezsignsignature_create_object_v1(self):
        """Test case for ezsignsignature_create_object_v1

        Create a new Ezsignsignature  # noqa: E501
        """
        pass

    def test_ezsignsignature_delete_object_v1(self):
        """Test case for ezsignsignature_delete_object_v1

        Delete an existing Ezsignsignature  # noqa: E501
        """
        pass

    def test_ezsignsignature_get_children_v1(self):
        """Test case for ezsignsignature_get_children_v1

        Retrieve an existing Ezsignsignature's children IDs  # noqa: E501
        """
        pass

    def test_ezsignsignature_get_object_v1(self):
        """Test case for ezsignsignature_get_object_v1

        Retrieve an existing Ezsignsignature  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
