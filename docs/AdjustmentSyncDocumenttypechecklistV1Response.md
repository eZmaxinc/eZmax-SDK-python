# AdjustmentSyncDocumenttypechecklistV1Response

Response for POST /1/object/adjustment/{pkiAdjustmentID}/syncDocumenttypechecklist

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**AdjustmentSyncDocumenttypechecklistV1ResponseMPayload**](AdjustmentSyncDocumenttypechecklistV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.adjustment_sync_documenttypechecklist_v1_response import AdjustmentSyncDocumenttypechecklistV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of AdjustmentSyncDocumenttypechecklistV1Response from a JSON string
adjustment_sync_documenttypechecklist_v1_response_instance = AdjustmentSyncDocumenttypechecklistV1Response.from_json(json)
# print the JSON string representation of the object
print(AdjustmentSyncDocumenttypechecklistV1Response.to_json())

# convert the object into a dict
adjustment_sync_documenttypechecklist_v1_response_dict = adjustment_sync_documenttypechecklist_v1_response_instance.to_dict()
# create an instance of AdjustmentSyncDocumenttypechecklistV1Response from a dict
adjustment_sync_documenttypechecklist_v1_response_from_dict = AdjustmentSyncDocumenttypechecklistV1Response.from_dict(adjustment_sync_documenttypechecklist_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


