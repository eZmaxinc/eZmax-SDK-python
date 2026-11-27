# TranqcontractSyncDocumenttypechecklistV1ResponseMPayload

Response for POST /1/object/tranqcontract/{pkiTranqcontractID}/syncDocumenttypechecklist

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_documenttypechecklist** | [**List[CustomDocumenttypechecklistResponse]**](CustomDocumenttypechecklistResponse.md) |  | 

## Example

```python
from eZmaxApi.models.tranqcontract_sync_documenttypechecklist_v1_response_m_payload import TranqcontractSyncDocumenttypechecklistV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of TranqcontractSyncDocumenttypechecklistV1ResponseMPayload from a JSON string
tranqcontract_sync_documenttypechecklist_v1_response_m_payload_instance = TranqcontractSyncDocumenttypechecklistV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(TranqcontractSyncDocumenttypechecklistV1ResponseMPayload.to_json())

# convert the object into a dict
tranqcontract_sync_documenttypechecklist_v1_response_m_payload_dict = tranqcontract_sync_documenttypechecklist_v1_response_m_payload_instance.to_dict()
# create an instance of TranqcontractSyncDocumenttypechecklistV1ResponseMPayload from a dict
tranqcontract_sync_documenttypechecklist_v1_response_m_payload_from_dict = TranqcontractSyncDocumenttypechecklistV1ResponseMPayload.from_dict(tranqcontract_sync_documenttypechecklist_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


