# SessionhistoryGetListV1Response

Response for GET /1/object/sessionhistory/getList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayloadGetList**](CommonResponseObjDebugPayloadGetList.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**SessionhistoryGetListV1ResponseMPayload**](SessionhistoryGetListV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.sessionhistory_get_list_v1_response import SessionhistoryGetListV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of SessionhistoryGetListV1Response from a JSON string
sessionhistory_get_list_v1_response_instance = SessionhistoryGetListV1Response.from_json(json)
# print the JSON string representation of the object
print SessionhistoryGetListV1Response.to_json()

# convert the object into a dict
sessionhistory_get_list_v1_response_dict = sessionhistory_get_list_v1_response_instance.to_dict()
# create an instance of SessionhistoryGetListV1Response from a dict
sessionhistory_get_list_v1_response_form_dict = sessionhistory_get_list_v1_response.from_dict(sessionhistory_get_list_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


