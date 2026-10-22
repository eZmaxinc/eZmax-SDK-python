# DocumenttypechecklistDeleteObjectV1Response

Response for DELETE /1/object/documenttypechecklist/{pkiDocumenttypechecklistID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.documenttypechecklist_delete_object_v1_response import DocumenttypechecklistDeleteObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of DocumenttypechecklistDeleteObjectV1Response from a JSON string
documenttypechecklist_delete_object_v1_response_instance = DocumenttypechecklistDeleteObjectV1Response.from_json(json)
# print the JSON string representation of the object
print(DocumenttypechecklistDeleteObjectV1Response.to_json())

# convert the object into a dict
documenttypechecklist_delete_object_v1_response_dict = documenttypechecklist_delete_object_v1_response_instance.to_dict()
# create an instance of DocumenttypechecklistDeleteObjectV1Response from a dict
documenttypechecklist_delete_object_v1_response_from_dict = DocumenttypechecklistDeleteObjectV1Response.from_dict(documenttypechecklist_delete_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


