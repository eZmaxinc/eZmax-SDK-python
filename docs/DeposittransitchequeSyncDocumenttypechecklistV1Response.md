# DeposittransitchequeSyncDocumenttypechecklistV1Response

Response for POST /1/object/deposittransitcheque/{pkiDeposittransitchequeID}/syncDocumenttypechecklist

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**DeposittransitchequeSyncDocumenttypechecklistV1ResponseMPayload**](DeposittransitchequeSyncDocumenttypechecklistV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.deposittransitcheque_sync_documenttypechecklist_v1_response import DeposittransitchequeSyncDocumenttypechecklistV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of DeposittransitchequeSyncDocumenttypechecklistV1Response from a JSON string
deposittransitcheque_sync_documenttypechecklist_v1_response_instance = DeposittransitchequeSyncDocumenttypechecklistV1Response.from_json(json)
# print the JSON string representation of the object
print(DeposittransitchequeSyncDocumenttypechecklistV1Response.to_json())

# convert the object into a dict
deposittransitcheque_sync_documenttypechecklist_v1_response_dict = deposittransitcheque_sync_documenttypechecklist_v1_response_instance.to_dict()
# create an instance of DeposittransitchequeSyncDocumenttypechecklistV1Response from a dict
deposittransitcheque_sync_documenttypechecklist_v1_response_from_dict = DeposittransitchequeSyncDocumenttypechecklistV1Response.from_dict(deposittransitcheque_sync_documenttypechecklist_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


