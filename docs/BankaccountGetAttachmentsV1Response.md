# BankaccountGetAttachmentsV1Response

Response for GET /1/object/bankaccount/{pkiBankaccountID}/getAttachments

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**BankaccountGetAttachmentsV1ResponseMPayload**](BankaccountGetAttachmentsV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.bankaccount_get_attachments_v1_response import BankaccountGetAttachmentsV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of BankaccountGetAttachmentsV1Response from a JSON string
bankaccount_get_attachments_v1_response_instance = BankaccountGetAttachmentsV1Response.from_json(json)
# print the JSON string representation of the object
print(BankaccountGetAttachmentsV1Response.to_json())

# convert the object into a dict
bankaccount_get_attachments_v1_response_dict = bankaccount_get_attachments_v1_response_instance.to_dict()
# create an instance of BankaccountGetAttachmentsV1Response from a dict
bankaccount_get_attachments_v1_response_from_dict = BankaccountGetAttachmentsV1Response.from_dict(bankaccount_get_attachments_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


