"""
    eZmax API Definition

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.1.5
    Contact: support-api@ezmax.ca
    Generated by: https://openapi-generator.tech
"""


import unittest

import eZmaxApi
from eZmaxApi.api.object_ezsignbulksend_api import ObjectEzsignbulksendApi  # noqa: E501


class TestObjectEzsignbulksendApi(unittest.TestCase):
    """ObjectEzsignbulksendApi unit test stubs"""

    def setUp(self):
        self.api = ObjectEzsignbulksendApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_ezsignbulksend_get_list_v1(self):
        """Test case for ezsignbulksend_get_list_v1

        Retrieve Ezsignbulksend list  # noqa: E501
        """
        pass

    def test_ezsignbulksend_get_object_v1(self):
        """Test case for ezsignbulksend_get_object_v1

        Retrieve an existing Ezsignbulksend  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
