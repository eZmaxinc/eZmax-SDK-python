# EzmaxinvoicinguserResponse

A Ezmaxinvoicinguser Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezmaxinvoicinguser_id** | **int** | The unique ID of the Ezmaxinvoicinguser | [optional] 
**fki_ezmaxinvoicing_id** | **int** | The unique ID of the Ezmaxinvoicing | [optional] 
**fki_billingentityinternal_id** | **int** | The unique ID of the Billingentityinternal. | 
**s_billingentityinternal_description_x** | **str** | The description of the Billingentityinternal in the language of the requester | 
**fki_user_id** | **int** | The unique ID of the User | 
**i_ezmaxinvoicinguser_ezsigndocument** | **int** | The number of ezsign documents | 
**b_ezmaxinvoicinguser_ezsignaccount** | **bool** | Whether there is an eZsign account | 
**b_ezmaxinvoicinguser_billableezsign** | **bool** | Whether it is billable for eZsign | 
**e_ezmaxinvoicinguser_variationezsign** | [**FieldEEzmaxinvoicinguserVariationezsign**](FieldEEzmaxinvoicinguserVariationezsign.md) |  | 

## Example

```python
from eZmaxApi.models.ezmaxinvoicinguser_response import EzmaxinvoicinguserResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EzmaxinvoicinguserResponse from a JSON string
ezmaxinvoicinguser_response_instance = EzmaxinvoicinguserResponse.from_json(json)
# print the JSON string representation of the object
print(EzmaxinvoicinguserResponse.to_json())

# convert the object into a dict
ezmaxinvoicinguser_response_dict = ezmaxinvoicinguser_response_instance.to_dict()
# create an instance of EzmaxinvoicinguserResponse from a dict
ezmaxinvoicinguser_response_from_dict = EzmaxinvoicinguserResponse.from_dict(ezmaxinvoicinguser_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


