# LeadSyncDocumenttypechecklistV1Response

Response for POST /1/object/lead/{pkiLeadID}/syncDocumenttypechecklist

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**LeadSyncDocumenttypechecklistV1ResponseMPayload**](LeadSyncDocumenttypechecklistV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.lead_sync_documenttypechecklist_v1_response import LeadSyncDocumenttypechecklistV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of LeadSyncDocumenttypechecklistV1Response from a JSON string
lead_sync_documenttypechecklist_v1_response_instance = LeadSyncDocumenttypechecklistV1Response.from_json(json)
# print the JSON string representation of the object
print(LeadSyncDocumenttypechecklistV1Response.to_json())

# convert the object into a dict
lead_sync_documenttypechecklist_v1_response_dict = lead_sync_documenttypechecklist_v1_response_instance.to_dict()
# create an instance of LeadSyncDocumenttypechecklistV1Response from a dict
lead_sync_documenttypechecklist_v1_response_from_dict = LeadSyncDocumenttypechecklistV1Response.from_dict(lead_sync_documenttypechecklist_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


