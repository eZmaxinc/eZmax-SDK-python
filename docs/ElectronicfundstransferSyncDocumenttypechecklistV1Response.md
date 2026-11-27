# ElectronicfundstransferSyncDocumenttypechecklistV1Response

Response for POST /1/object/electronicfundstransfer/{pkiElectronicfundstransferID}/syncDocumenttypechecklist

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**ElectronicfundstransferSyncDocumenttypechecklistV1ResponseMPayload**](ElectronicfundstransferSyncDocumenttypechecklistV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.electronicfundstransfer_sync_documenttypechecklist_v1_response import ElectronicfundstransferSyncDocumenttypechecklistV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of ElectronicfundstransferSyncDocumenttypechecklistV1Response from a JSON string
electronicfundstransfer_sync_documenttypechecklist_v1_response_instance = ElectronicfundstransferSyncDocumenttypechecklistV1Response.from_json(json)
# print the JSON string representation of the object
print(ElectronicfundstransferSyncDocumenttypechecklistV1Response.to_json())

# convert the object into a dict
electronicfundstransfer_sync_documenttypechecklist_v1_response_dict = electronicfundstransfer_sync_documenttypechecklist_v1_response_instance.to_dict()
# create an instance of ElectronicfundstransferSyncDocumenttypechecklistV1Response from a dict
electronicfundstransfer_sync_documenttypechecklist_v1_response_from_dict = ElectronicfundstransferSyncDocumenttypechecklistV1Response.from_dict(electronicfundstransfer_sync_documenttypechecklist_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


