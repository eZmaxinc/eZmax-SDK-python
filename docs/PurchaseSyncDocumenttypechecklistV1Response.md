# PurchaseSyncDocumenttypechecklistV1Response

Response for POST /1/object/purchase/{pkiPurchaseID}/syncDocumenttypechecklist

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**PurchaseSyncDocumenttypechecklistV1ResponseMPayload**](PurchaseSyncDocumenttypechecklistV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.purchase_sync_documenttypechecklist_v1_response import PurchaseSyncDocumenttypechecklistV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseSyncDocumenttypechecklistV1Response from a JSON string
purchase_sync_documenttypechecklist_v1_response_instance = PurchaseSyncDocumenttypechecklistV1Response.from_json(json)
# print the JSON string representation of the object
print(PurchaseSyncDocumenttypechecklistV1Response.to_json())

# convert the object into a dict
purchase_sync_documenttypechecklist_v1_response_dict = purchase_sync_documenttypechecklist_v1_response_instance.to_dict()
# create an instance of PurchaseSyncDocumenttypechecklistV1Response from a dict
purchase_sync_documenttypechecklist_v1_response_from_dict = PurchaseSyncDocumenttypechecklistV1Response.from_dict(purchase_sync_documenttypechecklist_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


