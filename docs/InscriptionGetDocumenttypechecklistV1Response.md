# InscriptionGetDocumenttypechecklistV1Response

Response for GET /1/object/inscription/{pkiInscriptionID}/getDocumenttypechecklist

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**InscriptionGetDocumenttypechecklistV1ResponseMPayload**](InscriptionGetDocumenttypechecklistV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.inscription_get_documenttypechecklist_v1_response import InscriptionGetDocumenttypechecklistV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of InscriptionGetDocumenttypechecklistV1Response from a JSON string
inscription_get_documenttypechecklist_v1_response_instance = InscriptionGetDocumenttypechecklistV1Response.from_json(json)
# print the JSON string representation of the object
print(InscriptionGetDocumenttypechecklistV1Response.to_json())

# convert the object into a dict
inscription_get_documenttypechecklist_v1_response_dict = inscription_get_documenttypechecklist_v1_response_instance.to_dict()
# create an instance of InscriptionGetDocumenttypechecklistV1Response from a dict
inscription_get_documenttypechecklist_v1_response_from_dict = InscriptionGetDocumenttypechecklistV1Response.from_dict(inscription_get_documenttypechecklist_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


