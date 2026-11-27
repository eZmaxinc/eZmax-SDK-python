# BankaccountSyncDocumenttypechecklistV1ResponseMPayload

Response for POST /1/object/bankaccount/{pkiBankaccountID}/syncDocumenttypechecklist

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_documenttypechecklist** | [**List[CustomDocumenttypechecklistResponse]**](CustomDocumenttypechecklistResponse.md) |  | 

## Example

```python
from eZmaxApi.models.bankaccount_sync_documenttypechecklist_v1_response_m_payload import BankaccountSyncDocumenttypechecklistV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of BankaccountSyncDocumenttypechecklistV1ResponseMPayload from a JSON string
bankaccount_sync_documenttypechecklist_v1_response_m_payload_instance = BankaccountSyncDocumenttypechecklistV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(BankaccountSyncDocumenttypechecklistV1ResponseMPayload.to_json())

# convert the object into a dict
bankaccount_sync_documenttypechecklist_v1_response_m_payload_dict = bankaccount_sync_documenttypechecklist_v1_response_m_payload_instance.to_dict()
# create an instance of BankaccountSyncDocumenttypechecklistV1ResponseMPayload from a dict
bankaccount_sync_documenttypechecklist_v1_response_m_payload_from_dict = BankaccountSyncDocumenttypechecklistV1ResponseMPayload.from_dict(bankaccount_sync_documenttypechecklist_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


