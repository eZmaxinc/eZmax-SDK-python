# CustomUserResponse

A User Object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_user_id** | **int** | The unique ID of the User | 
**s_user_lastname** | **str** | The last name of the user | 
**s_user_firstname** | **str** | The first name of the user | 
**s_email_address** | **str** | The email address. | 

## Example

```python
from eZmaxApi.models.custom_user_response import CustomUserResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomUserResponse from a JSON string
custom_user_response_instance = CustomUserResponse.from_json(json)
# print the JSON string representation of the object
print CustomUserResponse.to_json()

# convert the object into a dict
custom_user_response_dict = custom_user_response_instance.to_dict()
# create an instance of CustomUserResponse from a dict
custom_user_response_form_dict = custom_user_response.from_dict(custom_user_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


