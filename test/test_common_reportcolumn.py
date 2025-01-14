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

from eZmaxApi.models.common_reportcolumn import CommonReportcolumn

class TestCommonReportcolumn(unittest.TestCase):
    """CommonReportcolumn unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CommonReportcolumn:
        """Test CommonReportcolumn
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CommonReportcolumn`
        """
        model = CommonReportcolumn()
        if include_optional:
            return CommonReportcolumn(
                obj_reportcellstyle_default = eZmaxApi.models.common_reportcellstyle.Common-Reportcellstyle(
                    b_reportcellstyle_bordertop = True, 
                    b_reportcellstyle_borderbottom = True, 
                    b_reportcellstyle_borderleft = True, 
                    b_reportcellstyle_borderright = True, 
                    e_reportcell_horizontalalignment = 'Center', 
                    e_reportcell_verticalalignment = 'Bottom', 
                    e_reportcell_fontweight = 'Normal', 
                    e_reportcell_fontunderline = 'None', ),
                i_reportcolumn_width = 120
            )
        else:
            return CommonReportcolumn(
                obj_reportcellstyle_default = eZmaxApi.models.common_reportcellstyle.Common-Reportcellstyle(
                    b_reportcellstyle_bordertop = True, 
                    b_reportcellstyle_borderbottom = True, 
                    b_reportcellstyle_borderleft = True, 
                    b_reportcellstyle_borderright = True, 
                    e_reportcell_horizontalalignment = 'Center', 
                    e_reportcell_verticalalignment = 'Bottom', 
                    e_reportcell_fontweight = 'Normal', 
                    e_reportcell_fontunderline = 'None', ),
                i_reportcolumn_width = 120,
        )
        """

    def testCommonReportcolumn(self):
        """Test CommonReportcolumn"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
