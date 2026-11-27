# BuyercontractSyncDocumenttypechecklistV1ResponseMPayload

Response for POST /1/object/buyercontract/{pkiBuyercontractID}/syncDocumenttypechecklist

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_documenttypechecklist** | [**List[CustomDocumenttypechecklistResponse]**](CustomDocumenttypechecklistResponse.md) |  | 

## Example

```python
from eZmaxApi.models.buyercontract_sync_documenttypechecklist_v1_response_m_payload import BuyercontractSyncDocumenttypechecklistV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of BuyercontractSyncDocumenttypechecklistV1ResponseMPayload from a JSON string
buyercontract_sync_documenttypechecklist_v1_response_m_payload_instance = BuyercontractSyncDocumenttypechecklistV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(BuyercontractSyncDocumenttypechecklistV1ResponseMPayload.to_json())

# convert the object into a dict
buyercontract_sync_documenttypechecklist_v1_response_m_payload_dict = buyercontract_sync_documenttypechecklist_v1_response_m_payload_instance.to_dict()
# create an instance of BuyercontractSyncDocumenttypechecklistV1ResponseMPayload from a dict
buyercontract_sync_documenttypechecklist_v1_response_m_payload_from_dict = BuyercontractSyncDocumenttypechecklistV1ResponseMPayload.from_dict(buyercontract_sync_documenttypechecklist_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


