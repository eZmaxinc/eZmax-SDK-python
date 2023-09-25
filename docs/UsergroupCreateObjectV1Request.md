# UsergroupCreateObjectV1Request

Request for POST /1/object/usergroup

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_usergroup** | [**List[UsergroupRequestCompound]**](UsergroupRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.usergroup_create_object_v1_request import UsergroupCreateObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of UsergroupCreateObjectV1Request from a JSON string
usergroup_create_object_v1_request_instance = UsergroupCreateObjectV1Request.from_json(json)
# print the JSON string representation of the object
print UsergroupCreateObjectV1Request.to_json()

# convert the object into a dict
usergroup_create_object_v1_request_dict = usergroup_create_object_v1_request_instance.to_dict()
# create an instance of UsergroupCreateObjectV1Request from a dict
usergroup_create_object_v1_request_form_dict = usergroup_create_object_v1_request.from_dict(usergroup_create_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


