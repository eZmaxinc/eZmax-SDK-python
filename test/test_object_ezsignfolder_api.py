"""
    eZmax API Definition

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.1.2
    Contact: support-api@ezmax.ca
    Generated by: https://openapi-generator.tech
"""


import unittest

import eZmaxApi
from eZmaxApi.api.object_ezsignfolder_api import ObjectEzsignfolderApi  # noqa: E501


class TestObjectEzsignfolderApi(unittest.TestCase):
    """ObjectEzsignfolderApi unit test stubs"""

    def setUp(self):
        self.api = ObjectEzsignfolderApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_ezsignfolder_create_object_v1(self):
        """Test case for ezsignfolder_create_object_v1

        Create a new Ezsignfolder  # noqa: E501
        """
        pass

    def test_ezsignfolder_delete_object_v1(self):
        """Test case for ezsignfolder_delete_object_v1

        Delete an existing Ezsignfolder  # noqa: E501
        """
        pass

    def test_ezsignfolder_get_children_v1(self):
        """Test case for ezsignfolder_get_children_v1

        Retrieve an existing Ezsignfolder's children IDs  # noqa: E501
        """
        pass

    def test_ezsignfolder_get_forms_data_v1(self):
        """Test case for ezsignfolder_get_forms_data_v1

        Retrieve an existing Ezsignfolder's forms data  # noqa: E501
        """
        pass

    def test_ezsignfolder_get_list_v1(self):
        """Test case for ezsignfolder_get_list_v1

        Retrieve Ezsignfolder list  # noqa: E501
        """
        pass

    def test_ezsignfolder_get_object_v1(self):
        """Test case for ezsignfolder_get_object_v1

        Retrieve an existing Ezsignfolder  # noqa: E501
        """
        pass

    def test_ezsignfolder_send_v1(self):
        """Test case for ezsignfolder_send_v1

        Send the Ezsignfolder to the signatories for signature  # noqa: E501
        """
        pass

    def test_ezsignfolder_unsend_v1(self):
        """Test case for ezsignfolder_unsend_v1

        Unsend the Ezsignfolder  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
