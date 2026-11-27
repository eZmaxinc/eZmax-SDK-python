# PurchaseSyncDocumenttypechecklistV1ResponseMPayload

Response for POST /1/object/purchase/{pkiPurchaseID}/syncDocumenttypechecklist

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_documenttypechecklist** | [**List[CustomDocumenttypechecklistResponse]**](CustomDocumenttypechecklistResponse.md) |  | 

## Example

```python
from eZmaxApi.models.purchase_sync_documenttypechecklist_v1_response_m_payload import PurchaseSyncDocumenttypechecklistV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseSyncDocumenttypechecklistV1ResponseMPayload from a JSON string
purchase_sync_documenttypechecklist_v1_response_m_payload_instance = PurchaseSyncDocumenttypechecklistV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(PurchaseSyncDocumenttypechecklistV1ResponseMPayload.to_json())

# convert the object into a dict
purchase_sync_documenttypechecklist_v1_response_m_payload_dict = purchase_sync_documenttypechecklist_v1_response_m_payload_instance.to_dict()
# create an instance of PurchaseSyncDocumenttypechecklistV1ResponseMPayload from a dict
purchase_sync_documenttypechecklist_v1_response_m_payload_from_dict = PurchaseSyncDocumenttypechecklistV1ResponseMPayload.from_dict(purchase_sync_documenttypechecklist_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


