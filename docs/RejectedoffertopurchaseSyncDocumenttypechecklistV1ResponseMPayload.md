# RejectedoffertopurchaseSyncDocumenttypechecklistV1ResponseMPayload

Response for POST /1/object/rejectedoffertopurchase/{pkiRejectedoffertopurchaseID}/syncDocumenttypechecklist

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_documenttypechecklist** | [**List[CustomDocumenttypechecklistResponse]**](CustomDocumenttypechecklistResponse.md) |  | 

## Example

```python
from eZmaxApi.models.rejectedoffertopurchase_sync_documenttypechecklist_v1_response_m_payload import RejectedoffertopurchaseSyncDocumenttypechecklistV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of RejectedoffertopurchaseSyncDocumenttypechecklistV1ResponseMPayload from a JSON string
rejectedoffertopurchase_sync_documenttypechecklist_v1_response_m_payload_instance = RejectedoffertopurchaseSyncDocumenttypechecklistV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(RejectedoffertopurchaseSyncDocumenttypechecklistV1ResponseMPayload.to_json())

# convert the object into a dict
rejectedoffertopurchase_sync_documenttypechecklist_v1_response_m_payload_dict = rejectedoffertopurchase_sync_documenttypechecklist_v1_response_m_payload_instance.to_dict()
# create an instance of RejectedoffertopurchaseSyncDocumenttypechecklistV1ResponseMPayload from a dict
rejectedoffertopurchase_sync_documenttypechecklist_v1_response_m_payload_from_dict = RejectedoffertopurchaseSyncDocumenttypechecklistV1ResponseMPayload.from_dict(rejectedoffertopurchase_sync_documenttypechecklist_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


