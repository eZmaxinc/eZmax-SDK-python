# UserCreateObjectV2Request

Request for POST /1/object/user

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_user** | [**List[UserRequestCompoundV2]**](UserRequestCompoundV2.md) |  | 

## Example

```python
from eZmaxApi.models.user_create_object_v2_request import UserCreateObjectV2Request

# TODO update the JSON string below
json = "{}"
# create an instance of UserCreateObjectV2Request from a JSON string
user_create_object_v2_request_instance = UserCreateObjectV2Request.from_json(json)
# print the JSON string representation of the object
print(UserCreateObjectV2Request.to_json())

# convert the object into a dict
user_create_object_v2_request_dict = user_create_object_v2_request_instance.to_dict()
# create an instance of UserCreateObjectV2Request from a dict
user_create_object_v2_request_from_dict = UserCreateObjectV2Request.from_dict(user_create_object_v2_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


