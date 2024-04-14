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

from eZmaxApi.models.common_response_redirect_s_secretquestion_text_x import CommonResponseRedirectSSecretquestionTextX

class TestCommonResponseRedirectSSecretquestionTextX(unittest.TestCase):
    """CommonResponseRedirectSSecretquestionTextX unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CommonResponseRedirectSSecretquestionTextX:
        """Test CommonResponseRedirectSSecretquestionTextX
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CommonResponseRedirectSSecretquestionTextX`
        """
        model = CommonResponseRedirectSSecretquestionTextX()
        if include_optional:
            return CommonResponseRedirectSSecretquestionTextX(
                s_secretquestion_text_x = 'The name of the hospital in which you were born'
            )
        else:
            return CommonResponseRedirectSSecretquestionTextX(
                s_secretquestion_text_x = 'The name of the hospital in which you were born',
        )
        """

    def testCommonResponseRedirectSSecretquestionTextX(self):
        """Test CommonResponseRedirectSSecretquestionTextX"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
