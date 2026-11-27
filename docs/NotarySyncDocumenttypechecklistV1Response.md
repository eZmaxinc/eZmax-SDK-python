# NotarySyncDocumenttypechecklistV1Response

Response for POST /1/object/notary/{pkiNotaryID}/syncDocumenttypechecklist

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**NotarySyncDocumenttypechecklistV1ResponseMPayload**](NotarySyncDocumenttypechecklistV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.notary_sync_documenttypechecklist_v1_response import NotarySyncDocumenttypechecklistV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of NotarySyncDocumenttypechecklistV1Response from a JSON string
notary_sync_documenttypechecklist_v1_response_instance = NotarySyncDocumenttypechecklistV1Response.from_json(json)
# print the JSON string representation of the object
print(NotarySyncDocumenttypechecklistV1Response.to_json())

# convert the object into a dict
notary_sync_documenttypechecklist_v1_response_dict = notary_sync_documenttypechecklist_v1_response_instance.to_dict()
# create an instance of NotarySyncDocumenttypechecklistV1Response from a dict
notary_sync_documenttypechecklist_v1_response_from_dict = NotarySyncDocumenttypechecklistV1Response.from_dict(notary_sync_documenttypechecklist_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


