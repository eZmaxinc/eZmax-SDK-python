# BankaccountGetAttachmentsV1ResponseMPayload

Response for GET /1/object/bankaccount/{pkiBankaccountID}/getAttachments

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_attachmentdocumenttype** | [**List[CustomAttachmentdocumenttypeResponse]**](CustomAttachmentdocumenttypeResponse.md) |  | 

## Example

```python
from eZmaxApi.models.bankaccount_get_attachments_v1_response_m_payload import BankaccountGetAttachmentsV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of BankaccountGetAttachmentsV1ResponseMPayload from a JSON string
bankaccount_get_attachments_v1_response_m_payload_instance = BankaccountGetAttachmentsV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(BankaccountGetAttachmentsV1ResponseMPayload.to_json())

# convert the object into a dict
bankaccount_get_attachments_v1_response_m_payload_dict = bankaccount_get_attachments_v1_response_m_payload_instance.to_dict()
# create an instance of BankaccountGetAttachmentsV1ResponseMPayload from a dict
bankaccount_get_attachments_v1_response_m_payload_from_dict = BankaccountGetAttachmentsV1ResponseMPayload.from_dict(bankaccount_get_attachments_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


