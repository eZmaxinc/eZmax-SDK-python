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

from eZmaxApi.models.ezsigntemplate_get_object_v1_response_m_payload import EzsigntemplateGetObjectV1ResponseMPayload

class TestEzsigntemplateGetObjectV1ResponseMPayload(unittest.TestCase):
    """EzsigntemplateGetObjectV1ResponseMPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsigntemplateGetObjectV1ResponseMPayload:
        """Test EzsigntemplateGetObjectV1ResponseMPayload
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsigntemplateGetObjectV1ResponseMPayload`
        """
        model = EzsigntemplateGetObjectV1ResponseMPayload()
        if include_optional:
            return EzsigntemplateGetObjectV1ResponseMPayload(
                pki_ezsigntemplate_id = 36,
                fki_ezsigntemplatedocument_id = 133,
                fki_ezsignfoldertype_id = 5,
                fki_language_id = 2,
                s_language_name_x = 'English',
                s_ezsigntemplate_description = 'Standard Contract',
                s_ezsigntemplate_filenamepattern = 'Contract',
                b_ezsigntemplate_adminonly = True,
                s_ezsignfoldertype_name_x = 'Default',
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
                b_ezsigntemplate_editallowed = True,
                e_ezsigntemplate_type = 'Usergroup',
                obj_ezsigntemplatedocument = eZmaxApi.models.ezsigntemplatedocument_response.ezsigntemplatedocument-Response(
                    pki_ezsigntemplatedocument_id = 133, 
                    fki_ezsigntemplate_id = 36, 
                    s_ezsigntemplatedocument_name = 'Standard Contract', 
                    i_ezsigntemplatedocument_pagetotal = 5, 
                    i_ezsigntemplatedocument_signaturetotal = 8, 
                    b_ezsigntemplatedocument_hassignedsignatures = True, ),
                a_obj_ezsigntemplatesigner = [
                    eZmaxApi.models.ezsigntemplatesigner_response_compound.ezsigntemplatesigner-ResponseCompound()
                    ]
            )
        else:
            return EzsigntemplateGetObjectV1ResponseMPayload(
                pki_ezsigntemplate_id = 36,
                fki_language_id = 2,
                s_language_name_x = 'English',
                s_ezsigntemplate_description = 'Standard Contract',
                b_ezsigntemplate_adminonly = True,
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
                b_ezsigntemplate_editallowed = True,
                a_obj_ezsigntemplatesigner = [
                    eZmaxApi.models.ezsigntemplatesigner_response_compound.ezsigntemplatesigner-ResponseCompound()
                    ],
        )
        """

    def testEzsigntemplateGetObjectV1ResponseMPayload(self):
        """Test EzsigntemplateGetObjectV1ResponseMPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
