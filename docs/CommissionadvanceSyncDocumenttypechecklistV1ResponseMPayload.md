# CommissionadvanceSyncDocumenttypechecklistV1ResponseMPayload

Response for POST /1/object/commissionadvance/{pkiCommissionadvanceID}/syncDocumenttypechecklist

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_documenttypechecklist** | [**List[CustomDocumenttypechecklistResponse]**](CustomDocumenttypechecklistResponse.md) |  | 

## Example

```python
from eZmaxApi.models.commissionadvance_sync_documenttypechecklist_v1_response_m_payload import CommissionadvanceSyncDocumenttypechecklistV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of CommissionadvanceSyncDocumenttypechecklistV1ResponseMPayload from a JSON string
commissionadvance_sync_documenttypechecklist_v1_response_m_payload_instance = CommissionadvanceSyncDocumenttypechecklistV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(CommissionadvanceSyncDocumenttypechecklistV1ResponseMPayload.to_json())

# convert the object into a dict
commissionadvance_sync_documenttypechecklist_v1_response_m_payload_dict = commissionadvance_sync_documenttypechecklist_v1_response_m_payload_instance.to_dict()
# create an instance of CommissionadvanceSyncDocumenttypechecklistV1ResponseMPayload from a dict
commissionadvance_sync_documenttypechecklist_v1_response_m_payload_from_dict = CommissionadvanceSyncDocumenttypechecklistV1ResponseMPayload.from_dict(commissionadvance_sync_documenttypechecklist_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


