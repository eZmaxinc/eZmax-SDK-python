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

from eZmaxApi.models.common_get_report_v1_response_m_payload import CommonGetReportV1ResponseMPayload

class TestCommonGetReportV1ResponseMPayload(unittest.TestCase):
    """CommonGetReportV1ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CommonGetReportV1ResponseMPayload:
        """Test CommonGetReportV1ResponseMPayload
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CommonGetReportV1ResponseMPayload`
        """
        model = CommonGetReportV1ResponseMPayload()
        if include_optional:
            return CommonGetReportV1ResponseMPayload(
                obj_reportgroup = eZmaxApi.models.common_reportgroup.Common-Reportgroup(
                    a_obj_report = [
                        eZmaxApi.models.common_report.Common-Report(
                            a_obj_reportsection = [
                                eZmaxApi.models.common_reportsection.Common-Reportsection(
                                    a_obj_reportsubsection = [
                                        eZmaxApi.models.common_reportsubsection.Common-Reportsubsection(
                                            obj_reportsubsectionpart_header = eZmaxApi.models.common_reportsubsectionpart.Common-Reportsubsectionpart(
                                                e_reportsubsectionpart_type = 'Header', 
                                                a_obj_reportrow = [
                                                    eZmaxApi.models.common_reportrow.Common-Reportrow(
                                                        a_obj_reportcell = [
                                                            eZmaxApi.models.common_reportcell.Common-Reportcell(
                                                                i_reportcell_columnspan = 1, 
                                                                i_reportcell_rowspan = 1, )
                                                            ], 
                                                        i_reportrow_height = 20, )
                                                    ], ), 
                                            obj_reportsubsectionpart_body = eZmaxApi.models.common_reportsubsectionpart.Common-Reportsubsectionpart(
                                                e_reportsubsectionpart_type = 'Header', 
                                                a_obj_reportrow = [
                                                    eZmaxApi.models.common_reportrow.Common-Reportrow(
                                                        a_obj_reportcell = [
                                                            eZmaxApi.models.common_reportcell.Common-Reportcell(
                                                                i_reportcell_columnspan = 1, 
                                                                i_reportcell_rowspan = 1, )
                                                            ], 
                                                        i_reportrow_height = 20, )
                                                    ], ), 
                                            obj_reportsubsectionpart_footer = , )
                                        ], 
                                    a_obj_reportcolumn = [
                                        eZmaxApi.models.common_reportcolumn.Common-Reportcolumn(
                                            obj_reportcellstyle_default = eZmaxApi.models.common_reportcellstyle.Common-Reportcellstyle(
                                                b_reportcellstyle_bordertop = True, 
                                                b_reportcellstyle_borderbottom = True, 
                                                b_reportcellstyle_borderleft = True, 
                                                b_reportcellstyle_borderright = True, 
                                                e_reportcell_horizontalalignment = 'Center', 
                                                e_reportcell_verticalalignment = 'Bottom', 
                                                e_reportcell_fontweight = 'Normal', 
                                                e_reportcell_fontunderline = 'None', ), 
                                            i_reportcolumn_width = 120, )
                                        ], 
                                    e_reportsection_horizontalalignment = 'Center', 
                                    i_reportsection_columncount = 5, 
                                    i_reportsection_width = 1200, )
                                ], )
                        ], 
                    a_obj_reportcellstyle_custom = [
                        eZmaxApi.models.common_reportcellstyle.Common-Reportcellstyle(
                            b_reportcellstyle_bordertop = True, 
                            b_reportcellstyle_borderbottom = True, 
                            b_reportcellstyle_borderleft = True, 
                            b_reportcellstyle_borderright = True, 
                            e_reportcell_horizontalalignment = 'Center', 
                            e_reportcell_verticalalignment = 'Bottom', 
                            e_reportcell_fontweight = 'Normal', 
                            e_reportcell_fontunderline = 'None', )
                        ], )
            )
        else:
            return CommonGetReportV1ResponseMPayload(
                obj_reportgroup = eZmaxApi.models.common_reportgroup.Common-Reportgroup(
                    a_obj_report = [
                        eZmaxApi.models.common_report.Common-Report(
                            a_obj_reportsection = [
                                eZmaxApi.models.common_reportsection.Common-Reportsection(
                                    a_obj_reportsubsection = [
                                        eZmaxApi.models.common_reportsubsection.Common-Reportsubsection(
                                            obj_reportsubsectionpart_header = eZmaxApi.models.common_reportsubsectionpart.Common-Reportsubsectionpart(
                                                e_reportsubsectionpart_type = 'Header', 
                                                a_obj_reportrow = [
                                                    eZmaxApi.models.common_reportrow.Common-Reportrow(
                                                        a_obj_reportcell = [
                                                            eZmaxApi.models.common_reportcell.Common-Reportcell(
                                                                i_reportcell_columnspan = 1, 
                                                                i_reportcell_rowspan = 1, )
                                                            ], 
                                                        i_reportrow_height = 20, )
                                                    ], ), 
                                            obj_reportsubsectionpart_body = eZmaxApi.models.common_reportsubsectionpart.Common-Reportsubsectionpart(
                                                e_reportsubsectionpart_type = 'Header', 
                                                a_obj_reportrow = [
                                                    eZmaxApi.models.common_reportrow.Common-Reportrow(
                                                        a_obj_reportcell = [
                                                            eZmaxApi.models.common_reportcell.Common-Reportcell(
                                                                i_reportcell_columnspan = 1, 
                                                                i_reportcell_rowspan = 1, )
                                                            ], 
                                                        i_reportrow_height = 20, )
                                                    ], ), 
                                            obj_reportsubsectionpart_footer = , )
                                        ], 
                                    a_obj_reportcolumn = [
                                        eZmaxApi.models.common_reportcolumn.Common-Reportcolumn(
                                            obj_reportcellstyle_default = eZmaxApi.models.common_reportcellstyle.Common-Reportcellstyle(
                                                b_reportcellstyle_bordertop = True, 
                                                b_reportcellstyle_borderbottom = True, 
                                                b_reportcellstyle_borderleft = True, 
                                                b_reportcellstyle_borderright = True, 
                                                e_reportcell_horizontalalignment = 'Center', 
                                                e_reportcell_verticalalignment = 'Bottom', 
                                                e_reportcell_fontweight = 'Normal', 
                                                e_reportcell_fontunderline = 'None', ), 
                                            i_reportcolumn_width = 120, )
                                        ], 
                                    e_reportsection_horizontalalignment = 'Center', 
                                    i_reportsection_columncount = 5, 
                                    i_reportsection_width = 1200, )
                                ], )
                        ], 
                    a_obj_reportcellstyle_custom = [
                        eZmaxApi.models.common_reportcellstyle.Common-Reportcellstyle(
                            b_reportcellstyle_bordertop = True, 
                            b_reportcellstyle_borderbottom = True, 
                            b_reportcellstyle_borderleft = True, 
                            b_reportcellstyle_borderright = True, 
                            e_reportcell_horizontalalignment = 'Center', 
                            e_reportcell_verticalalignment = 'Bottom', 
                            e_reportcell_fontweight = 'Normal', 
                            e_reportcell_fontunderline = 'None', )
                        ], ),
        )
        """

    def testCommonGetReportV1ResponseMPayload(self):
        """Test CommonGetReportV1ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
