# BankaccountImportIntoEDMV1Request

Request for POST /1/object/bankaccount/{pkiBankaccountID}/importIntoEDM

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_attachment** | [**List[CustomAttachmentImportIntoEDMRequest]**](CustomAttachmentImportIntoEDMRequest.md) |  | 

## Example

```python
from eZmaxApi.models.bankaccount_import_into_edmv1_request import BankaccountImportIntoEDMV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of BankaccountImportIntoEDMV1Request from a JSON string
bankaccount_import_into_edmv1_request_instance = BankaccountImportIntoEDMV1Request.from_json(json)
# print the JSON string representation of the object
print(BankaccountImportIntoEDMV1Request.to_json())

# convert the object into a dict
bankaccount_import_into_edmv1_request_dict = bankaccount_import_into_edmv1_request_instance.to_dict()
# create an instance of BankaccountImportIntoEDMV1Request from a dict
bankaccount_import_into_edmv1_request_from_dict = BankaccountImportIntoEDMV1Request.from_dict(bankaccount_import_into_edmv1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


