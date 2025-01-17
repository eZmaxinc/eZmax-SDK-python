# UserEditObjectV1Response

Response for PUT /1/object/user/{pkiUserID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from eZmaxApi.models.user_edit_object_v1_response import UserEditObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of UserEditObjectV1Response from a JSON string
user_edit_object_v1_response_instance = UserEditObjectV1Response.from_json(json)
# print the JSON string representation of the object
print(UserEditObjectV1Response.to_json())

# convert the object into a dict
user_edit_object_v1_response_dict = user_edit_object_v1_response_instance.to_dict()
# create an instance of UserEditObjectV1Response from a dict
user_edit_object_v1_response_from_dict = UserEditObjectV1Response.from_dict(user_edit_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


