# UserstagedGetListV1Response

Response for GET /1/object/userstaged/getList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayloadGetList**](CommonResponseObjDebugPayloadGetList.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**UserstagedGetListV1ResponseMPayload**](UserstagedGetListV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.userstaged_get_list_v1_response import UserstagedGetListV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of UserstagedGetListV1Response from a JSON string
userstaged_get_list_v1_response_instance = UserstagedGetListV1Response.from_json(json)
# print the JSON string representation of the object
print(UserstagedGetListV1Response.to_json())

# convert the object into a dict
userstaged_get_list_v1_response_dict = userstaged_get_list_v1_response_instance.to_dict()
# create an instance of UserstagedGetListV1Response from a dict
userstaged_get_list_v1_response_form_dict = userstaged_get_list_v1_response.from_dict(userstaged_get_list_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


