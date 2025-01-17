# EzmaxinvoicingcontractResponseCompound

A Ezmaxinvoicingcontract Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezmaxinvoicingcontract_id** | **int** | The unique ID of the Ezmaxinvoicingcontract | 
**e_ezmaxinvoicingcontract_paymenttype** | [**FieldEEzmaxinvoicingcontractPaymenttype**](FieldEEzmaxinvoicingcontractPaymenttype.md) |  | 
**i_ezmaxinvoicingcontract_length** | **int** | The length in years of the Ezmaxinvoicingcontract | 
**dt_ezmaxinvoicingcontract_start** | **str** | The start date of the Ezmaxinvoicingcontract | 
**dt_ezmaxinvoicingcontract_end** | **str** | The end date of the Ezmaxinvoicingcontract | 
**d_ezmaxinvoicingcontract_license** | **str** | The price of the license | 
**d_ezmaxinvoicingcontract121qa** | **str** | The price for 121QA | 
**b_ezmaxinvoicingcontract_ezsignallagents** | **bool** | Whether eZsign is for all agents | 
**obj_audit** | [**CommonAudit**](CommonAudit.md) |  | 

## Example

```python
from eZmaxApi.models.ezmaxinvoicingcontract_response_compound import EzmaxinvoicingcontractResponseCompound

# TODO update the JSON string below
json = "{}"
# create an instance of EzmaxinvoicingcontractResponseCompound from a JSON string
ezmaxinvoicingcontract_response_compound_instance = EzmaxinvoicingcontractResponseCompound.from_json(json)
# print the JSON string representation of the object
print(EzmaxinvoicingcontractResponseCompound.to_json())

# convert the object into a dict
ezmaxinvoicingcontract_response_compound_dict = ezmaxinvoicingcontract_response_compound_instance.to_dict()
# create an instance of EzmaxinvoicingcontractResponseCompound from a dict
ezmaxinvoicingcontract_response_compound_from_dict = EzmaxinvoicingcontractResponseCompound.from_dict(ezmaxinvoicingcontract_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


