# BankaccountSyncDocumenttypechecklistV1Response

Response for POST /1/object/bankaccount/{pkiBankaccountID}/syncDocumenttypechecklist

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**BankaccountSyncDocumenttypechecklistV1ResponseMPayload**](BankaccountSyncDocumenttypechecklistV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.bankaccount_sync_documenttypechecklist_v1_response import BankaccountSyncDocumenttypechecklistV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of BankaccountSyncDocumenttypechecklistV1Response from a JSON string
bankaccount_sync_documenttypechecklist_v1_response_instance = BankaccountSyncDocumenttypechecklistV1Response.from_json(json)
# print the JSON string representation of the object
print(BankaccountSyncDocumenttypechecklistV1Response.to_json())

# convert the object into a dict
bankaccount_sync_documenttypechecklist_v1_response_dict = bankaccount_sync_documenttypechecklist_v1_response_instance.to_dict()
# create an instance of BankaccountSyncDocumenttypechecklistV1Response from a dict
bankaccount_sync_documenttypechecklist_v1_response_from_dict = BankaccountSyncDocumenttypechecklistV1Response.from_dict(bankaccount_sync_documenttypechecklist_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


