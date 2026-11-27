# TranqcontractSyncDocumenttypechecklistV1Response

Response for POST /1/object/tranqcontract/{pkiTranqcontractID}/syncDocumenttypechecklist

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**TranqcontractSyncDocumenttypechecklistV1ResponseMPayload**](TranqcontractSyncDocumenttypechecklistV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.tranqcontract_sync_documenttypechecklist_v1_response import TranqcontractSyncDocumenttypechecklistV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of TranqcontractSyncDocumenttypechecklistV1Response from a JSON string
tranqcontract_sync_documenttypechecklist_v1_response_instance = TranqcontractSyncDocumenttypechecklistV1Response.from_json(json)
# print the JSON string representation of the object
print(TranqcontractSyncDocumenttypechecklistV1Response.to_json())

# convert the object into a dict
tranqcontract_sync_documenttypechecklist_v1_response_dict = tranqcontract_sync_documenttypechecklist_v1_response_instance.to_dict()
# create an instance of TranqcontractSyncDocumenttypechecklistV1Response from a dict
tranqcontract_sync_documenttypechecklist_v1_response_from_dict = TranqcontractSyncDocumenttypechecklistV1Response.from_dict(tranqcontract_sync_documenttypechecklist_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


