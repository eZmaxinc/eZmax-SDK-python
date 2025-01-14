# CustomUserNameResponse

A User name Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s_user_lastname** | **str** | The last name of the user | 
**s_user_firstname** | **str** | The first name of the user | 

## Example

```python
from eZmaxApi.models.custom_user_name_response import CustomUserNameResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomUserNameResponse from a JSON string
custom_user_name_response_instance = CustomUserNameResponse.from_json(json)
# print the JSON string representation of the object
print(CustomUserNameResponse.to_json())

# convert the object into a dict
custom_user_name_response_dict = custom_user_name_response_instance.to_dict()
# create an instance of CustomUserNameResponse from a dict
custom_user_name_response_from_dict = CustomUserNameResponse.from_dict(custom_user_name_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


