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

from eZmaxApi.models.ezsignsignature_response_compound import EzsignsignatureResponseCompound

class TestEzsignsignatureResponseCompound(unittest.TestCase):
    """EzsignsignatureResponseCompound unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EzsignsignatureResponseCompound:
        """Test EzsignsignatureResponseCompound
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EzsignsignatureResponseCompound`
        """
        model = EzsignsignatureResponseCompound()
        if include_optional:
            return EzsignsignatureResponseCompound(
                pki_ezsignsignature_id = 49,
                fki_ezsigndocument_id = 97,
                fki_ezsignfoldersignerassociation_id = 20,
                fki_ezsignsigningreason_id = 194,
                fki_font_id = 1,
                s_ezsignsigningreason_description_x = 'I approve this document',
                i_ezsignpage_pagenumber = 1,
                i_ezsignsignature_x = 200,
                i_ezsignsignature_y = 300,
                i_ezsignsignature_height = 200,
                i_ezsignsignature_width = 200,
                i_ezsignsignature_step = 1,
                i_ezsignsignature_stepadjusted = 1,
                e_ezsignsignature_type = 'Name',
                t_ezsignsignature_tooltip = 'Please sign here if you agree to the terms',
                e_ezsignsignature_tooltipposition = 'TopLeft',
                e_ezsignsignature_font = 'Normal',
                i_ezsignsignature_validationstep = 1,
                s_ezsignsignature_attachmentdescription = 'Attachment',
                e_ezsignsignature_attachmentnamesource = 'Description',
                e_ezsignsignature_consultationtrigger = 'Manual',
                b_ezsignsignature_handwritten = True,
                b_ezsignsignature_reason = True,
                b_ezsignsignature_required = True,
                fki_ezsignfoldersignerassociation_id_validation = 20,
                dt_ezsignsignature_date = '2020-12-31 23:59:59',
                i_ezsignsignatureattachment_count = 7,
                s_ezsignsignature_description = 'Montreal',
                i_ezsignsignature_maxlength = 75,
                e_ezsignsignature_textvalidation = 'None',
                s_ezsignsignature_textvalidationcustommessage = 'Phone number',
                e_ezsignsignature_dependencyrequirement = 'AllOf',
                s_ezsignsignature_defaultvalue = 'Foo',
                s_ezsignsignature_regexp = '^[0-9]{9}$',
                obj_contact_name = eZmaxApi.models.custom_contact_name_response.Custom-ContactName-Response(
                    s_contact_firstname = 'John', 
                    s_contact_lastname = 'Doe', 
                    s_contact_company = 'eZmax Solutions Inc.', ),
                obj_contact_name_delegation = eZmaxApi.models.custom_contact_name_response.Custom-ContactName-Response(
                    s_contact_firstname = 'John', 
                    s_contact_lastname = 'Doe', 
                    s_contact_company = 'eZmax Solutions Inc.', ),
                obj_signature = eZmaxApi.models.signature_response_compound.signature-ResponseCompound(),
                dt_ezsignsignature_date_in_folder_timezone = '2020-12-31 23:59:59',
                b_ezsignsignature_customdate = True,
                a_obj_ezsignsignaturecustomdate = [
                    eZmaxApi.models.ezsignsignaturecustomdate_response_compound.ezsignsignaturecustomdate-ResponseCompound()
                    ],
                obj_creditcardtransaction = eZmaxApi.models.custom_creditcardtransaction_response.Custom-Creditcardtransaction-Response(
                    e_creditcardtype_codename = 'Visa', 
                    d_creditcardtransaction_amount = '167.58', 
                    s_creditcardtransaction_partiallydecryptednumber = 'XXXX XXXX XXXX 1234', 
                    s_creditcardtransaction_referencenumber = '651447854715478415', ),
                a_obj_ezsignelementdependency = [
                    eZmaxApi.models.ezsignelementdependency_response_compound.ezsignelementdependency-ResponseCompound()
                    ],
                obj_timezone = eZmaxApi.models.custom_timezone_with_code_response.Custom-TimezoneWithCode-Response(
                    s_timezone_name = '', 
                    s_code = 'EST', )
            )
        else:
            return EzsignsignatureResponseCompound(
                pki_ezsignsignature_id = 49,
                fki_ezsigndocument_id = 97,
                fki_ezsignfoldersignerassociation_id = 20,
                i_ezsignpage_pagenumber = 1,
                i_ezsignsignature_x = 200,
                i_ezsignsignature_y = 300,
                i_ezsignsignature_step = 1,
                e_ezsignsignature_type = 'Name',
                obj_contact_name = eZmaxApi.models.custom_contact_name_response.Custom-ContactName-Response(
                    s_contact_firstname = 'John', 
                    s_contact_lastname = 'Doe', 
                    s_contact_company = 'eZmax Solutions Inc.', ),
        )
        """

    def testEzsignsignatureResponseCompound(self):
        """Test EzsignsignatureResponseCompound"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
