# DeposittransitchequeSyncDocumenttypechecklistV1ResponseMPayload

Response for POST /1/object/deposittransitcheque/{pkiDeposittransitchequeID}/syncDocumenttypechecklist

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_documenttypechecklist** | [**List[CustomDocumenttypechecklistResponse]**](CustomDocumenttypechecklistResponse.md) |  | 

## Example

```python
from eZmaxApi.models.deposittransitcheque_sync_documenttypechecklist_v1_response_m_payload import DeposittransitchequeSyncDocumenttypechecklistV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of DeposittransitchequeSyncDocumenttypechecklistV1ResponseMPayload from a JSON string
deposittransitcheque_sync_documenttypechecklist_v1_response_m_payload_instance = DeposittransitchequeSyncDocumenttypechecklistV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(DeposittransitchequeSyncDocumenttypechecklistV1ResponseMPayload.to_json())

# convert the object into a dict
deposittransitcheque_sync_documenttypechecklist_v1_response_m_payload_dict = deposittransitcheque_sync_documenttypechecklist_v1_response_m_payload_instance.to_dict()
# create an instance of DeposittransitchequeSyncDocumenttypechecklistV1ResponseMPayload from a dict
deposittransitcheque_sync_documenttypechecklist_v1_response_m_payload_from_dict = DeposittransitchequeSyncDocumenttypechecklistV1ResponseMPayload.from_dict(deposittransitcheque_sync_documenttypechecklist_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


