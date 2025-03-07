# CustomCreditcardRequest

A Custom Creditcard Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fks_creditcardtoken_id** | **str** | The creditcard token identifier | 
**s_creditcard_cvv** | **str** | The creditcard card CVV | 
**obj_creditcarddetail** | [**CreditcarddetailRequest**](CreditcarddetailRequest.md) |  | 

## Example

```python
from eZmaxApi.models.custom_creditcard_request import CustomCreditcardRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CustomCreditcardRequest from a JSON string
custom_creditcard_request_instance = CustomCreditcardRequest.from_json(json)
# print the JSON string representation of the object
print(CustomCreditcardRequest.to_json())

# convert the object into a dict
custom_creditcard_request_dict = custom_creditcard_request_instance.to_dict()
# create an instance of CustomCreditcardRequest from a dict
custom_creditcard_request_from_dict = CustomCreditcardRequest.from_dict(custom_creditcard_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


