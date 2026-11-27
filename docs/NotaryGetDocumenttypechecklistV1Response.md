# NotaryGetDocumenttypechecklistV1Response

Response for GET /1/object/notary/{pkiNotaryID}/getDocumenttypechecklist

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**NotaryGetDocumenttypechecklistV1ResponseMPayload**](NotaryGetDocumenttypechecklistV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.notary_get_documenttypechecklist_v1_response import NotaryGetDocumenttypechecklistV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of NotaryGetDocumenttypechecklistV1Response from a JSON string
notary_get_documenttypechecklist_v1_response_instance = NotaryGetDocumenttypechecklistV1Response.from_json(json)
# print the JSON string representation of the object
print(NotaryGetDocumenttypechecklistV1Response.to_json())

# convert the object into a dict
notary_get_documenttypechecklist_v1_response_dict = notary_get_documenttypechecklist_v1_response_instance.to_dict()
# create an instance of NotaryGetDocumenttypechecklistV1Response from a dict
notary_get_documenttypechecklist_v1_response_from_dict = NotaryGetDocumenttypechecklistV1Response.from_dict(notary_get_documenttypechecklist_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


