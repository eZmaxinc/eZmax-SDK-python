"""
    eZmax API Definition (Full)

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.1.15
    Contact: support-api@ezmax.ca
    Generated by: https://openapi-generator.tech
"""


import unittest

import eZmaxApi
from eZmaxApi.api.object_branding_api import ObjectBrandingApi  # noqa: E501


class TestObjectBrandingApi(unittest.TestCase):
    """ObjectBrandingApi unit test stubs"""

    def setUp(self):
        self.api = ObjectBrandingApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_branding_create_object_v1(self):
        """Test case for branding_create_object_v1

        Create a new Branding  # noqa: E501
        """
        pass

    def test_branding_edit_object_v1(self):
        """Test case for branding_edit_object_v1

        Edit an existing Branding  # noqa: E501
        """
        pass

    def test_branding_get_autocomplete_v1(self):
        """Test case for branding_get_autocomplete_v1

        Retrieve Brandings and IDs  # noqa: E501
        """
        pass

    def test_branding_get_autocomplete_v2(self):
        """Test case for branding_get_autocomplete_v2

        Retrieve Brandings and IDs  # noqa: E501
        """
        pass

    def test_branding_get_list_v1(self):
        """Test case for branding_get_list_v1

        Retrieve Branding list  # noqa: E501
        """
        pass

    def test_branding_get_object_v1(self):
        """Test case for branding_get_object_v1

        Retrieve an existing Branding  # noqa: E501
        """
        pass

    def test_branding_get_object_v2(self):
        """Test case for branding_get_object_v2

        Retrieve an existing Branding  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
