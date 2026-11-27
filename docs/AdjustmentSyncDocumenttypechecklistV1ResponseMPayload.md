# AdjustmentSyncDocumenttypechecklistV1ResponseMPayload

Response for POST /1/object/adjustment/{pkiAdjustmentID}/syncDocumenttypechecklist

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_documenttypechecklist** | [**List[CustomDocumenttypechecklistResponse]**](CustomDocumenttypechecklistResponse.md) |  | 

## Example

```python
from eZmaxApi.models.adjustment_sync_documenttypechecklist_v1_response_m_payload import AdjustmentSyncDocumenttypechecklistV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of AdjustmentSyncDocumenttypechecklistV1ResponseMPayload from a JSON string
adjustment_sync_documenttypechecklist_v1_response_m_payload_instance = AdjustmentSyncDocumenttypechecklistV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(AdjustmentSyncDocumenttypechecklistV1ResponseMPayload.to_json())

# convert the object into a dict
adjustment_sync_documenttypechecklist_v1_response_m_payload_dict = adjustment_sync_documenttypechecklist_v1_response_m_payload_instance.to_dict()
# create an instance of AdjustmentSyncDocumenttypechecklistV1ResponseMPayload from a dict
adjustment_sync_documenttypechecklist_v1_response_m_payload_from_dict = AdjustmentSyncDocumenttypechecklistV1ResponseMPayload.from_dict(adjustment_sync_documenttypechecklist_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


