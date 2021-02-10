"""
    eZmax API Definition

    This API expose all the functionnalities for the eZmax and eZsign application.  We provide SDKs for customers. They are generated using OpenAPI codegen, we encourage customers to use them as we also provide samples for them.  You can choose to build your own implementation manually or can use any compatible OpenAPI 3.0 generator like Swagger Codegen, OpenAPI codegen or any commercial generators.  If you need helping understanding how to use this API, don't waste too much time looking for it. Contact support-api@ezmax.ca, we're here to help. We are developpers so we know programmers don't like bad documentation. If you don't find what you need in the documentation, let us know, we'll improve it and put you rapidly up on track.  # noqa: E501

    The version of the OpenAPI document: 1.0.29
    Contact: support-api@ezmax.ca
    Generated by: https://openapi-generator.tech
"""


import unittest

import eZmaxinc/eZmax-SDK-python
from eZmaxinc/eZmax-SDK-python.api.object_ezsignsignature_api import ObjectEzsignsignatureApi  # noqa: E501


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

    def test_ezsignsignature_edit_object_v1(self):
        """Test case for ezsignsignature_edit_object_v1

        Modify an existing Ezsignsignature  # noqa: E501
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
