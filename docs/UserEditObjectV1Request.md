# UserEditObjectV1Request

Request for PUT /1/object/user/{pkiUserID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_user** | [**UserRequestCompound**](UserRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.user_edit_object_v1_request import UserEditObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of UserEditObjectV1Request from a JSON string
user_edit_object_v1_request_instance = UserEditObjectV1Request.from_json(json)
# print the JSON string representation of the object
print(UserEditObjectV1Request.to_json())

# convert the object into a dict
user_edit_object_v1_request_dict = user_edit_object_v1_request_instance.to_dict()
# create an instance of UserEditObjectV1Request from a dict
user_edit_object_v1_request_form_dict = user_edit_object_v1_request.from_dict(user_edit_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


