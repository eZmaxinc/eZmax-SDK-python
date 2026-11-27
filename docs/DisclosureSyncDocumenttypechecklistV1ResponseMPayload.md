# DisclosureSyncDocumenttypechecklistV1ResponseMPayload

Response for POST /1/object/disclosure/{pkiDisclosureID}/syncDocumenttypechecklist

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_documenttypechecklist** | [**List[CustomDocumenttypechecklistResponse]**](CustomDocumenttypechecklistResponse.md) |  | 

## Example

```python
from eZmaxApi.models.disclosure_sync_documenttypechecklist_v1_response_m_payload import DisclosureSyncDocumenttypechecklistV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of DisclosureSyncDocumenttypechecklistV1ResponseMPayload from a JSON string
disclosure_sync_documenttypechecklist_v1_response_m_payload_instance = DisclosureSyncDocumenttypechecklistV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(DisclosureSyncDocumenttypechecklistV1ResponseMPayload.to_json())

# convert the object into a dict
disclosure_sync_documenttypechecklist_v1_response_m_payload_dict = disclosure_sync_documenttypechecklist_v1_response_m_payload_instance.to_dict()
# create an instance of DisclosureSyncDocumenttypechecklistV1ResponseMPayload from a dict
disclosure_sync_documenttypechecklist_v1_response_m_payload_from_dict = DisclosureSyncDocumenttypechecklistV1ResponseMPayload.from_dict(disclosure_sync_documenttypechecklist_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


