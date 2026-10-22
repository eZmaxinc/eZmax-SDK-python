# DocumenttypechecklistGetListV1Response

Response for GET /1/object/documenttypechecklist/getList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayloadGetList**](CommonResponseObjDebugPayloadGetList.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**DocumenttypechecklistGetListV1ResponseMPayload**](DocumenttypechecklistGetListV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.documenttypechecklist_get_list_v1_response import DocumenttypechecklistGetListV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of DocumenttypechecklistGetListV1Response from a JSON string
documenttypechecklist_get_list_v1_response_instance = DocumenttypechecklistGetListV1Response.from_json(json)
# print the JSON string representation of the object
print(DocumenttypechecklistGetListV1Response.to_json())

# convert the object into a dict
documenttypechecklist_get_list_v1_response_dict = documenttypechecklist_get_list_v1_response_instance.to_dict()
# create an instance of DocumenttypechecklistGetListV1Response from a dict
documenttypechecklist_get_list_v1_response_from_dict = DocumenttypechecklistGetListV1Response.from_dict(documenttypechecklist_get_list_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


