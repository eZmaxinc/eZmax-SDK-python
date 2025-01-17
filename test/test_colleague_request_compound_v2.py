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

from eZmaxApi.models.colleague_request_compound_v2 import ColleagueRequestCompoundV2

class TestColleagueRequestCompoundV2(unittest.TestCase):
    """ColleagueRequestCompoundV2 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ColleagueRequestCompoundV2:
        """Test ColleagueRequestCompoundV2
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ColleagueRequestCompoundV2`
        """
        model = ColleagueRequestCompoundV2()
        if include_optional:
            return ColleagueRequestCompoundV2(
                pki_colleague_id = 60,
                fki_user_id = 70,
                fki_user_id_colleague = 70,
                b_colleague_ezsignemail = False,
                b_colleague_financial = True,
                b_colleague_usecloneemail = True,
                b_colleague_attachment = True,
                b_colleague_canafe = True,
                b_colleague_permission = True,
                b_colleague_realestatecompleted = True,
                dt_colleague_from = '2020-12-31',
                dt_colleague_to = '2020-12-31',
                e_colleague_ezsign = 'Full',
                e_colleague_realestateinprogress = 'Create'
            )
        else:
            return ColleagueRequestCompoundV2(
                fki_user_id = 70,
                fki_user_id_colleague = 70,
                b_colleague_ezsignemail = False,
                b_colleague_financial = True,
                b_colleague_usecloneemail = True,
                b_colleague_attachment = True,
                b_colleague_canafe = True,
                b_colleague_permission = True,
                b_colleague_realestatecompleted = True,
                e_colleague_ezsign = 'Full',
                e_colleague_realestateinprogress = 'Create',
        )
        """

    def testColleagueRequestCompoundV2(self):
        """Test ColleagueRequestCompoundV2"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
