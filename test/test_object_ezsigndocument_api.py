"""
    eZmax API Definition (Full)

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.1.7
    Contact: support-api@ezmax.ca
    Generated by: https://openapi-generator.tech
"""


import unittest

import eZmaxApi
from eZmaxApi.api.object_ezsigndocument_api import ObjectEzsigndocumentApi  # noqa: E501


class TestObjectEzsigndocumentApi(unittest.TestCase):
    """ObjectEzsigndocumentApi unit test stubs"""

    def setUp(self):
        self.api = ObjectEzsigndocumentApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_ezsigndocument_apply_ezsigntemplate_v1(self):
        """Test case for ezsigndocument_apply_ezsigntemplate_v1

        Apply an Ezsigntemplate to the Ezsigndocument.  # noqa: E501
        """
        pass

    def test_ezsigndocument_apply_ezsigntemplate_v2(self):
        """Test case for ezsigndocument_apply_ezsigntemplate_v2

        Apply an Ezsigntemplate to the Ezsigndocument.  # noqa: E501
        """
        pass

    def test_ezsigndocument_create_object_v1(self):
        """Test case for ezsigndocument_create_object_v1

        Create a new Ezsigndocument  # noqa: E501
        """
        pass

    def test_ezsigndocument_create_object_v2(self):
        """Test case for ezsigndocument_create_object_v2

        Create a new Ezsigndocument  # noqa: E501
        """
        pass

    def test_ezsigndocument_delete_object_v1(self):
        """Test case for ezsigndocument_delete_object_v1

        Delete an existing Ezsigndocument  # noqa: E501
        """
        pass

    def test_ezsigndocument_edit_ezsignformfieldgroups_v1(self):
        """Test case for ezsigndocument_edit_ezsignformfieldgroups_v1

        Edit multiple Ezsignformfieldgroups  # noqa: E501
        """
        pass

    def test_ezsigndocument_edit_ezsignsignatures_v1(self):
        """Test case for ezsigndocument_edit_ezsignsignatures_v1

        Edit multiple Ezsignsignatures  # noqa: E501
        """
        pass

    def test_ezsigndocument_end_prematurely_v1(self):
        """Test case for ezsigndocument_end_prematurely_v1

        End prematurely  # noqa: E501
        """
        pass

    def test_ezsigndocument_get_actionable_elements_v1(self):
        """Test case for ezsigndocument_get_actionable_elements_v1

        Retrieve actionable elements for the Ezsigndocument  # noqa: E501
        """
        pass

    def test_ezsigndocument_get_download_url_v1(self):
        """Test case for ezsigndocument_get_download_url_v1

        Retrieve a URL to download documents.  # noqa: E501
        """
        pass

    def test_ezsigndocument_get_ezsignformfieldgroups_v1(self):
        """Test case for ezsigndocument_get_ezsignformfieldgroups_v1

        Retrieve an existing Ezsigndocument's Ezsignformfieldgroups  # noqa: E501
        """
        pass

    def test_ezsigndocument_get_ezsignpages_v1(self):
        """Test case for ezsigndocument_get_ezsignpages_v1

        Retrieve an existing Ezsigndocument's Ezsignpages  # noqa: E501
        """
        pass

    def test_ezsigndocument_get_ezsignsignatures_v1(self):
        """Test case for ezsigndocument_get_ezsignsignatures_v1

        Retrieve an existing Ezsigndocument's Ezsignsignatures  # noqa: E501
        """
        pass

    def test_ezsigndocument_get_form_data_v1(self):
        """Test case for ezsigndocument_get_form_data_v1

        Retrieve an existing Ezsigndocument's Form Data  # noqa: E501
        """
        pass

    def test_ezsigndocument_get_object_v1(self):
        """Test case for ezsigndocument_get_object_v1

        Retrieve an existing Ezsigndocument  # noqa: E501
        """
        pass

    def test_ezsigndocument_get_temporary_proof_v1(self):
        """Test case for ezsigndocument_get_temporary_proof_v1

        Retrieve the temporary proof  # noqa: E501
        """
        pass

    def test_ezsigndocument_get_words_positions_v1(self):
        """Test case for ezsigndocument_get_words_positions_v1

        Retrieve positions X,Y of given words from a Ezsigndocument  # noqa: E501
        """
        pass

    def test_ezsigndocument_patch_object_v1(self):
        """Test case for ezsigndocument_patch_object_v1

        Patch an existing Ezsigndocument  # noqa: E501
        """
        pass

    def test_ezsigndocument_unsend_v1(self):
        """Test case for ezsigndocument_unsend_v1

        Unsend the Ezsigndocument  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
