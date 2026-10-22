# DocumenttypeGetListV1Response

Response for GET /1/object/documenttype/getList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayloadGetList**](CommonResponseObjDebugPayloadGetList.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**DocumenttypeGetListV1ResponseMPayload**](DocumenttypeGetListV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.documenttype_get_list_v1_response import DocumenttypeGetListV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of DocumenttypeGetListV1Response from a JSON string
documenttype_get_list_v1_response_instance = DocumenttypeGetListV1Response.from_json(json)
# print the JSON string representation of the object
print(DocumenttypeGetListV1Response.to_json())

# convert the object into a dict
documenttype_get_list_v1_response_dict = documenttype_get_list_v1_response_instance.to_dict()
# create an instance of DocumenttypeGetListV1Response from a dict
documenttype_get_list_v1_response_from_dict = DocumenttypeGetListV1Response.from_dict(documenttype_get_list_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


