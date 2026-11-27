# LeadSyncDocumenttypechecklistV1ResponseMPayload

Response for POST /1/object/lead/{pkiLeadID}/syncDocumenttypechecklist

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_documenttypechecklist** | [**List[CustomDocumenttypechecklistResponse]**](CustomDocumenttypechecklistResponse.md) |  | 

## Example

```python
from eZmaxApi.models.lead_sync_documenttypechecklist_v1_response_m_payload import LeadSyncDocumenttypechecklistV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of LeadSyncDocumenttypechecklistV1ResponseMPayload from a JSON string
lead_sync_documenttypechecklist_v1_response_m_payload_instance = LeadSyncDocumenttypechecklistV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(LeadSyncDocumenttypechecklistV1ResponseMPayload.to_json())

# convert the object into a dict
lead_sync_documenttypechecklist_v1_response_m_payload_dict = lead_sync_documenttypechecklist_v1_response_m_payload_instance.to_dict()
# create an instance of LeadSyncDocumenttypechecklistV1ResponseMPayload from a dict
lead_sync_documenttypechecklist_v1_response_m_payload_from_dict = LeadSyncDocumenttypechecklistV1ResponseMPayload.from_dict(lead_sync_documenttypechecklist_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


