# UsergroupexternalGetListV1Response

Response for GET /1/object/usergroupexternal/getList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayloadGetList**](CommonResponseObjDebugPayloadGetList.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**UsergroupexternalGetListV1ResponseMPayload**](UsergroupexternalGetListV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.usergroupexternal_get_list_v1_response import UsergroupexternalGetListV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of UsergroupexternalGetListV1Response from a JSON string
usergroupexternal_get_list_v1_response_instance = UsergroupexternalGetListV1Response.from_json(json)
# print the JSON string representation of the object
print(UsergroupexternalGetListV1Response.to_json())

# convert the object into a dict
usergroupexternal_get_list_v1_response_dict = usergroupexternal_get_list_v1_response_instance.to_dict()
# create an instance of UsergroupexternalGetListV1Response from a dict
usergroupexternal_get_list_v1_response_form_dict = usergroupexternal_get_list_v1_response.from_dict(usergroupexternal_get_list_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


