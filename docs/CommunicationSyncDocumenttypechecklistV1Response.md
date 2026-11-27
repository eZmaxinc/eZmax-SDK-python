# CommunicationSyncDocumenttypechecklistV1Response

Response for POST /1/object/communication/{pkiCommunicationID}/syncDocumenttypechecklist

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**CommunicationSyncDocumenttypechecklistV1ResponseMPayload**](CommunicationSyncDocumenttypechecklistV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.communication_sync_documenttypechecklist_v1_response import CommunicationSyncDocumenttypechecklistV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of CommunicationSyncDocumenttypechecklistV1Response from a JSON string
communication_sync_documenttypechecklist_v1_response_instance = CommunicationSyncDocumenttypechecklistV1Response.from_json(json)
# print the JSON string representation of the object
print(CommunicationSyncDocumenttypechecklistV1Response.to_json())

# convert the object into a dict
communication_sync_documenttypechecklist_v1_response_dict = communication_sync_documenttypechecklist_v1_response_instance.to_dict()
# create an instance of CommunicationSyncDocumenttypechecklistV1Response from a dict
communication_sync_documenttypechecklist_v1_response_from_dict = CommunicationSyncDocumenttypechecklistV1Response.from_dict(communication_sync_documenttypechecklist_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


