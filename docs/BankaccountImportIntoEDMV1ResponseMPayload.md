# BankaccountImportIntoEDMV1ResponseMPayload

Payload for POST /1/object/bankaccount/{pkiBankaccountID}/importIntoEDM

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_attachment** | [**List[CustomAttachmentImportIntoEDMResponse]**](CustomAttachmentImportIntoEDMResponse.md) |  | 

## Example

```python
from eZmaxApi.models.bankaccount_import_into_edmv1_response_m_payload import BankaccountImportIntoEDMV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of BankaccountImportIntoEDMV1ResponseMPayload from a JSON string
bankaccount_import_into_edmv1_response_m_payload_instance = BankaccountImportIntoEDMV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(BankaccountImportIntoEDMV1ResponseMPayload.to_json())

# convert the object into a dict
bankaccount_import_into_edmv1_response_m_payload_dict = bankaccount_import_into_edmv1_response_m_payload_instance.to_dict()
# create an instance of BankaccountImportIntoEDMV1ResponseMPayload from a dict
bankaccount_import_into_edmv1_response_m_payload_from_dict = BankaccountImportIntoEDMV1ResponseMPayload.from_dict(bankaccount_import_into_edmv1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


