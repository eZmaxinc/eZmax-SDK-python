# CustomTimezoneWithCodeResponse

Generic AutocompleteElement Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s_timezone_name** | **str** | The Name of timezone | 
**s_code** | **str** | The Code of the time | 

## Example

```python
from eZmaxApi.models.custom_timezone_with_code_response import CustomTimezoneWithCodeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomTimezoneWithCodeResponse from a JSON string
custom_timezone_with_code_response_instance = CustomTimezoneWithCodeResponse.from_json(json)
# print the JSON string representation of the object
print(CustomTimezoneWithCodeResponse.to_json())

# convert the object into a dict
custom_timezone_with_code_response_dict = custom_timezone_with_code_response_instance.to_dict()
# create an instance of CustomTimezoneWithCodeResponse from a dict
custom_timezone_with_code_response_from_dict = CustomTimezoneWithCodeResponse.from_dict(custom_timezone_with_code_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


