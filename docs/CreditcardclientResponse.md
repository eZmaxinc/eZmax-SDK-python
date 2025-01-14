# CreditcardclientResponse

A Creditcardclient Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_creditcardclient_id** | **int** | The unique ID of the Creditcardclient | 
**fki_creditcarddetail_id** | **int** | The unique ID of the Creditcarddetail | 
**b_creditcardclientrelation_isdefault** | **bool** | Whether if it&#39;s the creditcardclient is the default one | 
**s_creditcardclient_description** | **str** | The description of the Creditcardclient | 
**b_creditcardclient_allowedcompanypayment** | **bool** | Whether if it&#39;s an allowedagencypayment | 
**b_creditcardclient_allowedtranquillit** | **bool** | Whether if it&#39;s an allowedtranquillit | 
**obj_creditcarddetail** | [**CreditcarddetailResponseCompound**](CreditcarddetailResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.creditcardclient_response import CreditcardclientResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreditcardclientResponse from a JSON string
creditcardclient_response_instance = CreditcardclientResponse.from_json(json)
# print the JSON string representation of the object
print(CreditcardclientResponse.to_json())

# convert the object into a dict
creditcardclient_response_dict = creditcardclient_response_instance.to_dict()
# create an instance of CreditcardclientResponse from a dict
creditcardclient_response_from_dict = CreditcardclientResponse.from_dict(creditcardclient_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


