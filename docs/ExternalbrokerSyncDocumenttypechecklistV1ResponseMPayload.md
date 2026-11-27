# ExternalbrokerSyncDocumenttypechecklistV1ResponseMPayload

Response for POST /1/object/externalbroker/{pkiExternalbrokerID}/syncDocumenttypechecklist

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_documenttypechecklist** | [**List[CustomDocumenttypechecklistResponse]**](CustomDocumenttypechecklistResponse.md) |  | 

## Example

```python
from eZmaxApi.models.externalbroker_sync_documenttypechecklist_v1_response_m_payload import ExternalbrokerSyncDocumenttypechecklistV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalbrokerSyncDocumenttypechecklistV1ResponseMPayload from a JSON string
externalbroker_sync_documenttypechecklist_v1_response_m_payload_instance = ExternalbrokerSyncDocumenttypechecklistV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(ExternalbrokerSyncDocumenttypechecklistV1ResponseMPayload.to_json())

# convert the object into a dict
externalbroker_sync_documenttypechecklist_v1_response_m_payload_dict = externalbroker_sync_documenttypechecklist_v1_response_m_payload_instance.to_dict()
# create an instance of ExternalbrokerSyncDocumenttypechecklistV1ResponseMPayload from a dict
externalbroker_sync_documenttypechecklist_v1_response_m_payload_from_dict = ExternalbrokerSyncDocumenttypechecklistV1ResponseMPayload.from_dict(externalbroker_sync_documenttypechecklist_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


