# UsergroupCreateObjectV1Response

Response for POST /1/object/usergroup

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m_payload** | [**UsergroupCreateObjectV1ResponseMPayload**](UsergroupCreateObjectV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.usergroup_create_object_v1_response import UsergroupCreateObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of UsergroupCreateObjectV1Response from a JSON string
usergroup_create_object_v1_response_instance = UsergroupCreateObjectV1Response.from_json(json)
# print the JSON string representation of the object
print(UsergroupCreateObjectV1Response.to_json())

# convert the object into a dict
usergroup_create_object_v1_response_dict = usergroup_create_object_v1_response_instance.to_dict()
# create an instance of UsergroupCreateObjectV1Response from a dict
usergroup_create_object_v1_response_from_dict = UsergroupCreateObjectV1Response.from_dict(usergroup_create_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


