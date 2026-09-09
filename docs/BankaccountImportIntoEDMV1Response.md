# BankaccountImportIntoEDMV1Response

Response for POST /1/object/bankaccount/{pkiBankaccountID}/importIntoEDM

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**BankaccountImportIntoEDMV1ResponseMPayload**](BankaccountImportIntoEDMV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.bankaccount_import_into_edmv1_response import BankaccountImportIntoEDMV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of BankaccountImportIntoEDMV1Response from a JSON string
bankaccount_import_into_edmv1_response_instance = BankaccountImportIntoEDMV1Response.from_json(json)
# print the JSON string representation of the object
print(BankaccountImportIntoEDMV1Response.to_json())

# convert the object into a dict
bankaccount_import_into_edmv1_response_dict = bankaccount_import_into_edmv1_response_instance.to_dict()
# create an instance of BankaccountImportIntoEDMV1Response from a dict
bankaccount_import_into_edmv1_response_from_dict = BankaccountImportIntoEDMV1Response.from_dict(bankaccount_import_into_edmv1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


