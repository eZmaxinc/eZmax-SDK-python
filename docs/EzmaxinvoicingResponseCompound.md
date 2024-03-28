# EzmaxinvoicingResponseCompound

A Ezmaxinvoicing Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezmaxinvoicing_id** | **int** | The unique ID of the Ezmaxinvoicing | [optional] 
**fki_ezmaxinvoicingcontract_id** | **int** | The unique ID of the Ezmaxinvoicingcontract | 
**fki_ezmaxpricing_id** | **int** | The unique ID of the Ezmaxpricing | 
**fki_systemconfigurationtype_id** | **int** | The unique ID of the Systemconfigurationtype | 
**s_systemconfigurationtype_description_x** | **str** | The description of the Systemconfigurationtype in the language of the requester | 
**yyyymm_ezmaxinvoicing** | **str** | The YYYYMM period of the Ezmaxinvoicing | 
**i_ezmaxinvoicing_days** | **int** | The number of days invoiced | 
**e_ezmaxinvoicing_paymenttype** | [**FieldEEzmaxinvoicingPaymenttype**](FieldEEzmaxinvoicingPaymenttype.md) |  | 
**d_ezmaxinvoicing_rebatepaymenttype** | **str** | The percentage of rebate depending of the payment type | 
**i_ezmaxinvoicing_contractlength** | **int** | The length of the contract in years | 
**d_ezmaxinvoicing_rebatecontractlength** | **str** | The percentage of rebate depending of the contract length | 
**b_ezmaxinvoicing_rebate_ezsignallagents** | **bool** | Whether the rebate for eZsign is for all agents | 
**obj_audit** | [**CommonAudit**](CommonAudit.md) |  | [optional] 
**obj_ezmaxinvoicingcontract** | [**EzmaxinvoicingcontractResponseCompound**](EzmaxinvoicingcontractResponseCompound.md) |  | 
**obj_ezmaxpricing** | [**CustomEzmaxpricingResponse**](CustomEzmaxpricingResponse.md) |  | 
**a_obj_ezmaxinvoicingsummaryglobal** | [**List[EzmaxinvoicingsummaryglobalResponseCompound]**](EzmaxinvoicingsummaryglobalResponseCompound.md) |  | 
**a_obj_ezmaxinvoicingsummaryexternal** | [**List[EzmaxinvoicingsummaryexternalResponseCompound]**](EzmaxinvoicingsummaryexternalResponseCompound.md) |  | 
**a_obj_ezmaxinvoicingsummaryinternal** | [**List[EzmaxinvoicingsummaryinternalResponseCompound]**](EzmaxinvoicingsummaryinternalResponseCompound.md) |  | 
**a_obj_ezmaxinvoicingagent** | [**List[EzmaxinvoicingagentResponseCompound]**](EzmaxinvoicingagentResponseCompound.md) |  | 
**a_obj_ezmaxinvoicinguser** | [**List[EzmaxinvoicinguserResponseCompound]**](EzmaxinvoicinguserResponseCompound.md) |  | 
**a_obj_ezmaxinvoicingezsignfolder** | [**List[CustomEzmaxinvoicingEzsignfolderResponse]**](CustomEzmaxinvoicingEzsignfolderResponse.md) |  | 
**a_obj_ezmaxinvoicingezsigndocument** | [**List[CustomEzmaxinvoicingEzsigndocumentResponse]**](CustomEzmaxinvoicingEzsigndocumentResponse.md) |  | 

## Example

```python
from eZmaxApi.models.ezmaxinvoicing_response_compound import EzmaxinvoicingResponseCompound

# TODO update the JSON string below
json = "{}"
# create an instance of EzmaxinvoicingResponseCompound from a JSON string
ezmaxinvoicing_response_compound_instance = EzmaxinvoicingResponseCompound.from_json(json)
# print the JSON string representation of the object
print(EzmaxinvoicingResponseCompound.to_json())

# convert the object into a dict
ezmaxinvoicing_response_compound_dict = ezmaxinvoicing_response_compound_instance.to_dict()
# create an instance of EzmaxinvoicingResponseCompound from a dict
ezmaxinvoicing_response_compound_form_dict = ezmaxinvoicing_response_compound.from_dict(ezmaxinvoicing_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


