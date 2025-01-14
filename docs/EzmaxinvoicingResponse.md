# EzmaxinvoicingResponse

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

## Example

```python
from eZmaxApi.models.ezmaxinvoicing_response import EzmaxinvoicingResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EzmaxinvoicingResponse from a JSON string
ezmaxinvoicing_response_instance = EzmaxinvoicingResponse.from_json(json)
# print the JSON string representation of the object
print(EzmaxinvoicingResponse.to_json())

# convert the object into a dict
ezmaxinvoicing_response_dict = ezmaxinvoicing_response_instance.to_dict()
# create an instance of EzmaxinvoicingResponse from a dict
ezmaxinvoicing_response_from_dict = EzmaxinvoicingResponse.from_dict(ezmaxinvoicing_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


