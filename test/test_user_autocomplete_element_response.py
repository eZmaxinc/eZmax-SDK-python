"""
    eZmax API Definition (Full)

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.1.14
    Contact: support-api@ezmax.ca
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import eZmaxApi
from eZmaxApi.model.field_e_user_type import FieldEUserType
from eZmaxApi.model.field_pki_user_id import FieldPkiUserID
globals()['FieldEUserType'] = FieldEUserType
globals()['FieldPkiUserID'] = FieldPkiUserID
from eZmaxApi.model.user_autocomplete_element_response import UserAutocompleteElementResponse


class TestUserAutocompleteElementResponse(unittest.TestCase):
    """UserAutocompleteElementResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testUserAutocompleteElementResponse(self):
        """Test UserAutocompleteElementResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = UserAutocompleteElementResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
