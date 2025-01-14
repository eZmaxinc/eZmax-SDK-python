# CommonResponseWarning

Generic Warning Message

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s_warning_message** | **str** | More detail about the warning | 
**e_warning_code** | **str** | The warning code. See documentation for valid values | 

## Example

```python
from eZmaxApi.models.common_response_warning import CommonResponseWarning

# TODO update the JSON string below
json = "{}"
# create an instance of CommonResponseWarning from a JSON string
common_response_warning_instance = CommonResponseWarning.from_json(json)
# print the JSON string representation of the object
print(CommonResponseWarning.to_json())

# convert the object into a dict
common_response_warning_dict = common_response_warning_instance.to_dict()
# create an instance of CommonResponseWarning from a dict
common_response_warning_from_dict = CommonResponseWarning.from_dict(common_response_warning_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


