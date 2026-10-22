# DocumenttypechecklistGetObjectV2Response

Response for GET /2/object/documenttypechecklist/{pkiDocumenttypechecklistID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**DocumenttypechecklistGetObjectV2ResponseMPayload**](DocumenttypechecklistGetObjectV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.documenttypechecklist_get_object_v2_response import DocumenttypechecklistGetObjectV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of DocumenttypechecklistGetObjectV2Response from a JSON string
documenttypechecklist_get_object_v2_response_instance = DocumenttypechecklistGetObjectV2Response.from_json(json)
# print the JSON string representation of the object
print(DocumenttypechecklistGetObjectV2Response.to_json())

# convert the object into a dict
documenttypechecklist_get_object_v2_response_dict = documenttypechecklist_get_object_v2_response_instance.to_dict()
# create an instance of DocumenttypechecklistGetObjectV2Response from a dict
documenttypechecklist_get_object_v2_response_from_dict = DocumenttypechecklistGetObjectV2Response.from_dict(documenttypechecklist_get_object_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


