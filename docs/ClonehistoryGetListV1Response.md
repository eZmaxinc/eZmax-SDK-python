# ClonehistoryGetListV1Response

Response for GET /1/object/clonehistory/getList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayloadGetList**](CommonResponseObjDebugPayloadGetList.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**ClonehistoryGetListV1ResponseMPayload**](ClonehistoryGetListV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.clonehistory_get_list_v1_response import ClonehistoryGetListV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of ClonehistoryGetListV1Response from a JSON string
clonehistory_get_list_v1_response_instance = ClonehistoryGetListV1Response.from_json(json)
# print the JSON string representation of the object
print ClonehistoryGetListV1Response.to_json()

# convert the object into a dict
clonehistory_get_list_v1_response_dict = clonehistory_get_list_v1_response_instance.to_dict()
# create an instance of ClonehistoryGetListV1Response from a dict
clonehistory_get_list_v1_response_form_dict = clonehistory_get_list_v1_response.from_dict(clonehistory_get_list_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


