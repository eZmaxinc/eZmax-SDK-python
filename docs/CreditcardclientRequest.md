# CreditcardclientRequest

A Creditcardclient Object

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
from eZmaxApi.models.creditcardclient_request import CreditcardclientRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreditcardclientRequest from a JSON string
creditcardclient_request_instance = CreditcardclientRequest.from_json(json)
# print the JSON string representation of the object
print(CreditcardclientRequest.to_json())

# convert the object into a dict
creditcardclient_request_dict = creditcardclient_request_instance.to_dict()
# create an instance of CreditcardclientRequest from a dict
creditcardclient_request_form_dict = creditcardclient_request.from_dict(creditcardclient_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


