# InscriptiontempSyncDocumenttypechecklistV1ResponseMPayload

Response for POST /1/object/inscriptiontemp/{pkiInscriptiontempID}/syncDocumenttypechecklist

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_documenttypechecklist** | [**List[CustomDocumenttypechecklistResponse]**](CustomDocumenttypechecklistResponse.md) |  | 

## Example

```python
from eZmaxApi.models.inscriptiontemp_sync_documenttypechecklist_v1_response_m_payload import InscriptiontempSyncDocumenttypechecklistV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of InscriptiontempSyncDocumenttypechecklistV1ResponseMPayload from a JSON string
inscriptiontemp_sync_documenttypechecklist_v1_response_m_payload_instance = InscriptiontempSyncDocumenttypechecklistV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(InscriptiontempSyncDocumenttypechecklistV1ResponseMPayload.to_json())

# convert the object into a dict
inscriptiontemp_sync_documenttypechecklist_v1_response_m_payload_dict = inscriptiontemp_sync_documenttypechecklist_v1_response_m_payload_instance.to_dict()
# create an instance of InscriptiontempSyncDocumenttypechecklistV1ResponseMPayload from a dict
inscriptiontemp_sync_documenttypechecklist_v1_response_m_payload_from_dict = InscriptiontempSyncDocumenttypechecklistV1ResponseMPayload.from_dict(inscriptiontemp_sync_documenttypechecklist_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


