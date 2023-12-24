# UserCreateObjectV1Request

Request for POST /1/object/user

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_user** | [**List[UserRequestCompound]**](UserRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.user_create_object_v1_request import UserCreateObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of UserCreateObjectV1Request from a JSON string
user_create_object_v1_request_instance = UserCreateObjectV1Request.from_json(json)
# print the JSON string representation of the object
print UserCreateObjectV1Request.to_json()

# convert the object into a dict
user_create_object_v1_request_dict = user_create_object_v1_request_instance.to_dict()
# create an instance of UserCreateObjectV1Request from a dict
user_create_object_v1_request_form_dict = user_create_object_v1_request.from_dict(user_create_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


