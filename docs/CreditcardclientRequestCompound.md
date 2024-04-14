# CreditcardclientRequestCompound

A Creditcardclient Object and children

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_creditcardclient_id** | **int** | The unique ID of the Creditcardclient | [optional] 
**fks_creditcardtoken_id** | **str** | The creditcard token identifier | [optional] 
**b_creditcardclientrelation_isdefault** | **bool** | Whether if it&#39;s an relationisdefault | 
**s_creditcardclient_description** | **str** | The description of the Creditcardclient | 
**b_creditcardclient_isactive** | **bool** | Whether the creditcardclient is active or not | 
**b_creditcardclient_allowedagencypayment** | **bool** | Whether if it&#39;s an allowedagencypayment | 
**b_creditcardclient_allowedroyallepageprotection** | **bool** | Whether if it&#39;s an allowedroyallepageprotection | 
**b_creditcardclient_allowedtranquillit** | **bool** | Whether if it&#39;s an allowedtranquillit | 
**obj_creditcarddetail** | [**CreditcarddetailRequest**](CreditcarddetailRequest.md) |  | 
**s_creditcardclient_cvv** | **str** | The creditcard card CVV | 

## Example

```python
from eZmaxApi.models.creditcardclient_request_compound import CreditcardclientRequestCompound

# TODO update the JSON string below
json = "{}"
# create an instance of CreditcardclientRequestCompound from a JSON string
creditcardclient_request_compound_instance = CreditcardclientRequestCompound.from_json(json)
# print the JSON string representation of the object
print(CreditcardclientRequestCompound.to_json())

# convert the object into a dict
creditcardclient_request_compound_dict = creditcardclient_request_compound_instance.to_dict()
# create an instance of CreditcardclientRequestCompound from a dict
creditcardclient_request_compound_form_dict = creditcardclient_request_compound.from_dict(creditcardclient_request_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


