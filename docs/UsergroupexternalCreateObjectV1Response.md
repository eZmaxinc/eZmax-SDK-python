# UsergroupexternalCreateObjectV1Response

Response for POST /1/object/usergroupexternal

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m_payload** | [**UsergroupexternalCreateObjectV1ResponseMPayload**](UsergroupexternalCreateObjectV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.usergroupexternal_create_object_v1_response import UsergroupexternalCreateObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of UsergroupexternalCreateObjectV1Response from a JSON string
usergroupexternal_create_object_v1_response_instance = UsergroupexternalCreateObjectV1Response.from_json(json)
# print the JSON string representation of the object
print(UsergroupexternalCreateObjectV1Response.to_json())

# convert the object into a dict
usergroupexternal_create_object_v1_response_dict = usergroupexternal_create_object_v1_response_instance.to_dict()
# create an instance of UsergroupexternalCreateObjectV1Response from a dict
usergroupexternal_create_object_v1_response_from_dict = UsergroupexternalCreateObjectV1Response.from_dict(usergroupexternal_create_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


