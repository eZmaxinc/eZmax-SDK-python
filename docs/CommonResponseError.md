# CommonResponseError

Generic Error Message

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s_error_message** | **str** | The message giving details about the error | 
**e_error_code** | [**FieldEErrorCode**](FieldEErrorCode.md) |  | 

## Example

```python
from eZmaxApi.models.common_response_error import CommonResponseError

# TODO update the JSON string below
json = "{}"
# create an instance of CommonResponseError from a JSON string
common_response_error_instance = CommonResponseError.from_json(json)
# print the JSON string representation of the object
print(CommonResponseError.to_json())

# convert the object into a dict
common_response_error_dict = common_response_error_instance.to_dict()
# create an instance of CommonResponseError from a dict
common_response_error_form_dict = common_response_error.from_dict(common_response_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


