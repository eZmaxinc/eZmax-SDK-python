# RejectedoffertopurchaseSyncDocumenttypechecklistV1Response

Response for POST /1/object/rejectedoffertopurchase/{pkiRejectedoffertopurchaseID}/syncDocumenttypechecklist

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**RejectedoffertopurchaseSyncDocumenttypechecklistV1ResponseMPayload**](RejectedoffertopurchaseSyncDocumenttypechecklistV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.rejectedoffertopurchase_sync_documenttypechecklist_v1_response import RejectedoffertopurchaseSyncDocumenttypechecklistV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of RejectedoffertopurchaseSyncDocumenttypechecklistV1Response from a JSON string
rejectedoffertopurchase_sync_documenttypechecklist_v1_response_instance = RejectedoffertopurchaseSyncDocumenttypechecklistV1Response.from_json(json)
# print the JSON string representation of the object
print(RejectedoffertopurchaseSyncDocumenttypechecklistV1Response.to_json())

# convert the object into a dict
rejectedoffertopurchase_sync_documenttypechecklist_v1_response_dict = rejectedoffertopurchase_sync_documenttypechecklist_v1_response_instance.to_dict()
# create an instance of RejectedoffertopurchaseSyncDocumenttypechecklistV1Response from a dict
rejectedoffertopurchase_sync_documenttypechecklist_v1_response_from_dict = RejectedoffertopurchaseSyncDocumenttypechecklistV1Response.from_dict(rejectedoffertopurchase_sync_documenttypechecklist_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


