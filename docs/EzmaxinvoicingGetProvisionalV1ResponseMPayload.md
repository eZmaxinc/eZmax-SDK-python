# EzmaxinvoicingGetProvisionalV1ResponseMPayload

Payload for GET /1/object/ezmaxinvoicing/getProvisional

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fki_ezmaxinvoicingcontract_id** | [**FieldPkiEzmaxinvoicingcontractID**](FieldPkiEzmaxinvoicingcontractID.md) |  | 
**fki_ezmaxpricing_id** | [**FieldPkiEzmaxpricingID**](FieldPkiEzmaxpricingID.md) |  | 
**fki_systemconfigurationtype_id** | [**FieldPkiSystemconfigurationtypeID**](FieldPkiSystemconfigurationtypeID.md) |  | 
**s_systemconfigurationtype_description_x** | **str** | The description of the Systemconfigurationtype in the language of the requester | 
**yyyymm_ezmaxinvoicing** | [**FieldYyyymmEzmaxinvoicing**](FieldYyyymmEzmaxinvoicing.md) |  | 
**i_ezmaxinvoicing_days** | [**FieldIEzmaxinvoicingDays**](FieldIEzmaxinvoicingDays.md) |  | 
**e_ezmaxinvoicing_paymenttype** | [**FieldEEzmaxinvoicingPaymenttype**](FieldEEzmaxinvoicingPaymenttype.md) |  | 
**d_ezmaxinvoicing_rebatepaymenttype** | [**FieldDEzmaxinvoicingRebatepaymenttype**](FieldDEzmaxinvoicingRebatepaymenttype.md) |  | 
**i_ezmaxinvoicing_contractlength** | [**FieldIEzmaxinvoicingContractlength**](FieldIEzmaxinvoicingContractlength.md) |  | 
**d_ezmaxinvoicing_rebatecontractlength** | [**FieldDEzmaxinvoicingRebatecontractlength**](FieldDEzmaxinvoicingRebatecontractlength.md) |  | 
**b_ezmaxinvoicing_rebate_ezsignallagents** | **bool** | Whether the rebate for eZsign is for all agents | 
**obj_ezmaxinvoicingcontract** | [**EzmaxinvoicingcontractResponseCompound**](EzmaxinvoicingcontractResponseCompound.md) |  | 
**obj_ezmaxpricing** | [**CustomEzmaxpricingResponse**](CustomEzmaxpricingResponse.md) |  | 
**a_obj_ezmaxinvoicingsummaryglobal** | [**[EzmaxinvoicingsummaryglobalResponseCompound]**](EzmaxinvoicingsummaryglobalResponseCompound.md) |  | 
**a_obj_ezmaxinvoicingsummaryexternal** | [**[EzmaxinvoicingsummaryexternalResponseCompound]**](EzmaxinvoicingsummaryexternalResponseCompound.md) |  | 
**a_obj_ezmaxinvoicingsummaryinternal** | [**[EzmaxinvoicingsummaryinternalResponseCompound]**](EzmaxinvoicingsummaryinternalResponseCompound.md) |  | 
**a_obj_ezmaxinvoicingagent** | [**[EzmaxinvoicingagentResponseCompound]**](EzmaxinvoicingagentResponseCompound.md) |  | 
**a_obj_ezmaxinvoicinguser** | [**[EzmaxinvoicinguserResponseCompound]**](EzmaxinvoicinguserResponseCompound.md) |  | 
**a_obj_ezmaxinvoicingezsignfolder** | [**[CustomEzmaxinvoicingEzsignfolderResponse]**](CustomEzmaxinvoicingEzsignfolderResponse.md) |  | 
**a_obj_ezmaxinvoicingezsigndocument** | [**[CustomEzmaxinvoicingEzsigndocumentResponse]**](CustomEzmaxinvoicingEzsigndocumentResponse.md) |  | 
**pki_ezmaxinvoicing_id** | [**FieldPkiEzmaxinvoicingID**](FieldPkiEzmaxinvoicingID.md) |  | [optional] 
**obj_audit** | [**CommonAudit**](CommonAudit.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


