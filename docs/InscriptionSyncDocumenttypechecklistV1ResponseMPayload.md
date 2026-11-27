# InscriptionSyncDocumenttypechecklistV1ResponseMPayload

Response for POST /1/object/inscription/{pkiInscriptionID}/syncDocumenttypechecklist

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_documenttypechecklist** | [**List[CustomDocumenttypechecklistResponse]**](CustomDocumenttypechecklistResponse.md) |  | 

## Example

```python
from eZmaxApi.models.inscription_sync_documenttypechecklist_v1_response_m_payload import InscriptionSyncDocumenttypechecklistV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of InscriptionSyncDocumenttypechecklistV1ResponseMPayload from a JSON string
inscription_sync_documenttypechecklist_v1_response_m_payload_instance = InscriptionSyncDocumenttypechecklistV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(InscriptionSyncDocumenttypechecklistV1ResponseMPayload.to_json())

# convert the object into a dict
inscription_sync_documenttypechecklist_v1_response_m_payload_dict = inscription_sync_documenttypechecklist_v1_response_m_payload_instance.to_dict()
# create an instance of InscriptionSyncDocumenttypechecklistV1ResponseMPayload from a dict
inscription_sync_documenttypechecklist_v1_response_m_payload_from_dict = InscriptionSyncDocumenttypechecklistV1ResponseMPayload.from_dict(inscription_sync_documenttypechecklist_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


