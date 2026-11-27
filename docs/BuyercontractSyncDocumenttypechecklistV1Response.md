# BuyercontractSyncDocumenttypechecklistV1Response

Response for POST /1/object/buyercontract/{pkiBuyercontractID}/syncDocumenttypechecklist

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**BuyercontractSyncDocumenttypechecklistV1ResponseMPayload**](BuyercontractSyncDocumenttypechecklistV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.buyercontract_sync_documenttypechecklist_v1_response import BuyercontractSyncDocumenttypechecklistV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of BuyercontractSyncDocumenttypechecklistV1Response from a JSON string
buyercontract_sync_documenttypechecklist_v1_response_instance = BuyercontractSyncDocumenttypechecklistV1Response.from_json(json)
# print the JSON string representation of the object
print(BuyercontractSyncDocumenttypechecklistV1Response.to_json())

# convert the object into a dict
buyercontract_sync_documenttypechecklist_v1_response_dict = buyercontract_sync_documenttypechecklist_v1_response_instance.to_dict()
# create an instance of BuyercontractSyncDocumenttypechecklistV1Response from a dict
buyercontract_sync_documenttypechecklist_v1_response_from_dict = BuyercontractSyncDocumenttypechecklistV1Response.from_dict(buyercontract_sync_documenttypechecklist_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


