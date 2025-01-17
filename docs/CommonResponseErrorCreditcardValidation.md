# CommonResponseErrorCreditcardValidation

Generic Error Message

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_creditcardtransactionresponse** | [**CustomCreditcardtransactionresponseResponse**](CustomCreditcardtransactionresponseResponse.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.common_response_error_creditcard_validation import CommonResponseErrorCreditcardValidation

# TODO update the JSON string below
json = "{}"
# create an instance of CommonResponseErrorCreditcardValidation from a JSON string
common_response_error_creditcard_validation_instance = CommonResponseErrorCreditcardValidation.from_json(json)
# print the JSON string representation of the object
print(CommonResponseErrorCreditcardValidation.to_json())

# convert the object into a dict
common_response_error_creditcard_validation_dict = common_response_error_creditcard_validation_instance.to_dict()
# create an instance of CommonResponseErrorCreditcardValidation from a dict
common_response_error_creditcard_validation_from_dict = CommonResponseErrorCreditcardValidation.from_dict(common_response_error_creditcard_validation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


