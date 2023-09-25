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

from eZmaxApi.models.ezmaxinvoicingcontract_response import EzmaxinvoicingcontractResponse  # noqa: E501

class TestEzmaxinvoicingcontractResponse(unittest.TestCase):
    """EzmaxinvoicingcontractResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzmaxinvoicingcontractResponse:
        """Test EzmaxinvoicingcontractResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzmaxinvoicingcontractResponse`
        """
        model = EzmaxinvoicingcontractResponse()  # noqa: E501
        if include_optional:
            return EzmaxinvoicingcontractResponse(
                pki_ezmaxinvoicingcontract_id = 28,
                e_ezmaxinvoicingcontract_paymenttype = 'Cheque',
                i_ezmaxinvoicingcontract_length = 3,
                dt_ezmaxinvoicingcontract_start = '2020-12-31',
                dt_ezmaxinvoicingcontract_end = '2020-12-31',
                d_ezmaxinvoicingcontract_license = '335.42',
                d_ezmaxinvoicingcontract121qa = '295.48',
                b_ezmaxinvoicingcontract_ezsignallagents = True,
                obj_audit = eZmaxApi.models.common_audit.Common-Audit(
                    obj_auditdetail_created = eZmaxApi.models.common_auditdetail.Common-Auditdetail(
                        fki_user_id = 70, 
                        fki_apikey_id = 99, 
                        s_user_loginname = 'JohnDoe', 
                        s_user_lastname = 'Doe', 
                        s_user_firstname = 'John', 
                        s_apikey_description_x = 'Project X', 
                        dt_auditdetail_date = '2020-12-31 23:59:59', ), 
                    obj_auditdetail_modified = eZmaxApi.models.common_auditdetail.Common-Auditdetail(
                        fki_user_id = 70, 
                        fki_apikey_id = 99, 
                        s_user_loginname = 'JohnDoe', 
                        s_user_lastname = 'Doe', 
                        s_user_firstname = 'John', 
                        s_apikey_description_x = 'Project X', 
                        dt_auditdetail_date = '2020-12-31 23:59:59', ), )
            )
        else:
            return EzmaxinvoicingcontractResponse(
                pki_ezmaxinvoicingcontract_id = 28,
                e_ezmaxinvoicingcontract_paymenttype = 'Cheque',
                i_ezmaxinvoicingcontract_length = 3,
                dt_ezmaxinvoicingcontract_start = '2020-12-31',
                dt_ezmaxinvoicingcontract_end = '2020-12-31',
                d_ezmaxinvoicingcontract_license = '335.42',
                d_ezmaxinvoicingcontract121qa = '295.48',
                b_ezmaxinvoicingcontract_ezsignallagents = True,
                obj_audit = eZmaxApi.models.common_audit.Common-Audit(
                    obj_auditdetail_created = eZmaxApi.models.common_auditdetail.Common-Auditdetail(
                        fki_user_id = 70, 
                        fki_apikey_id = 99, 
                        s_user_loginname = 'JohnDoe', 
                        s_user_lastname = 'Doe', 
                        s_user_firstname = 'John', 
                        s_apikey_description_x = 'Project X', 
                        dt_auditdetail_date = '2020-12-31 23:59:59', ), 
                    obj_auditdetail_modified = eZmaxApi.models.common_auditdetail.Common-Auditdetail(
                        fki_user_id = 70, 
                        fki_apikey_id = 99, 
                        s_user_loginname = 'JohnDoe', 
                        s_user_lastname = 'Doe', 
                        s_user_firstname = 'John', 
                        s_apikey_description_x = 'Project X', 
                        dt_auditdetail_date = '2020-12-31 23:59:59', ), ),
        )
        """

    def testEzmaxinvoicingcontractResponse(self):
        """Test EzmaxinvoicingcontractResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
