# CustomCreditcardtransactionresponseResponse

A custom Creditcardtransactionresponse Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s_creditcardtransaction_is_ocode** | **str** | The ISO code | 
**s_creditcardtransaction_responsecode** | **str** | The response code | 
**s_creditcardtransaction_responseterminalmessage** | **str** | The terminal response message | 
**e_creditcardtransaction_avsresult** | [**FieldECreditcardtransactionAvsresult**](FieldECreditcardtransactionAvsresult.md) |  | [optional] 
**e_creditcardtransaction_cvdresult** | [**FieldECreditcardtransactionCvdresult**](FieldECreditcardtransactionCvdresult.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.custom_creditcardtransactionresponse_response import CustomCreditcardtransactionresponseResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomCreditcardtransactionresponseResponse from a JSON string
custom_creditcardtransactionresponse_response_instance = CustomCreditcardtransactionresponseResponse.from_json(json)
# print the JSON string representation of the object
print(CustomCreditcardtransactionresponseResponse.to_json())

# convert the object into a dict
custom_creditcardtransactionresponse_response_dict = custom_creditcardtransactionresponse_response_instance.to_dict()
# create an instance of CustomCreditcardtransactionresponseResponse from a dict
custom_creditcardtransactionresponse_response_from_dict = CustomCreditcardtransactionresponseResponse.from_dict(custom_creditcardtransactionresponse_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


