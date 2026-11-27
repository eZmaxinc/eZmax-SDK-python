# NotarySyncDocumenttypechecklistV1ResponseMPayload

Response for POST /1/object/notary/{pkiNotaryID}/syncDocumenttypechecklist

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_documenttypechecklist** | [**List[CustomDocumenttypechecklistResponse]**](CustomDocumenttypechecklistResponse.md) |  | 

## Example

```python
from eZmaxApi.models.notary_sync_documenttypechecklist_v1_response_m_payload import NotarySyncDocumenttypechecklistV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of NotarySyncDocumenttypechecklistV1ResponseMPayload from a JSON string
notary_sync_documenttypechecklist_v1_response_m_payload_instance = NotarySyncDocumenttypechecklistV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(NotarySyncDocumenttypechecklistV1ResponseMPayload.to_json())

# convert the object into a dict
notary_sync_documenttypechecklist_v1_response_m_payload_dict = notary_sync_documenttypechecklist_v1_response_m_payload_instance.to_dict()
# create an instance of NotarySyncDocumenttypechecklistV1ResponseMPayload from a dict
notary_sync_documenttypechecklist_v1_response_m_payload_from_dict = NotarySyncDocumenttypechecklistV1ResponseMPayload.from_dict(notary_sync_documenttypechecklist_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


