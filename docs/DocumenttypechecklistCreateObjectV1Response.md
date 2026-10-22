# DocumenttypechecklistCreateObjectV1Response

Response for POST /1/object/documenttypechecklist

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**DocumenttypechecklistCreateObjectV1ResponseMPayload**](DocumenttypechecklistCreateObjectV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.documenttypechecklist_create_object_v1_response import DocumenttypechecklistCreateObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of DocumenttypechecklistCreateObjectV1Response from a JSON string
documenttypechecklist_create_object_v1_response_instance = DocumenttypechecklistCreateObjectV1Response.from_json(json)
# print the JSON string representation of the object
print(DocumenttypechecklistCreateObjectV1Response.to_json())

# convert the object into a dict
documenttypechecklist_create_object_v1_response_dict = documenttypechecklist_create_object_v1_response_instance.to_dict()
# create an instance of DocumenttypechecklistCreateObjectV1Response from a dict
documenttypechecklist_create_object_v1_response_from_dict = DocumenttypechecklistCreateObjectV1Response.from_dict(documenttypechecklist_create_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


