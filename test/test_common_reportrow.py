# coding: utf-8

"""
    eZmax API Definition (Full)

    This API expose all the functionnalities for the eZmax and eZsign applications.

    The version of the OpenAPI document: 1.2.0
    Contact: support-api@ezmax.ca
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from eZmaxApi.models.common_reportrow import CommonReportrow

class TestCommonReportrow(unittest.TestCase):
    """CommonReportrow unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CommonReportrow:
        """Test CommonReportrow
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CommonReportrow`
        """
        model = CommonReportrow()
        if include_optional:
            return CommonReportrow(
                a_obj_reportcell = [
                    eZmaxApi.models.common_reportcell.Common-Reportcell(
                        i_reportcell_columnspan = 1, 
                        i_reportcell_rowspan = 1, )
                    ],
                i_reportrow_height = 20
            )
        else:
            return CommonReportrow(
                a_obj_reportcell = [
                    eZmaxApi.models.common_reportcell.Common-Reportcell(
                        i_reportcell_columnspan = 1, 
                        i_reportcell_rowspan = 1, )
                    ],
                i_reportrow_height = 20,
        )
        """

    def testCommonReportrow(self):
        """Test CommonReportrow"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
