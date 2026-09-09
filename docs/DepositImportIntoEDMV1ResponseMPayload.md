# DepositImportIntoEDMV1ResponseMPayload

Payload for POST /1/object/deposit/{pkiDepositID}/importIntoEDM

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_attachment** | [**List[CustomAttachmentImportIntoEDMResponse]**](CustomAttachmentImportIntoEDMResponse.md) |  | 

## Example

```python
from eZmaxApi.models.deposit_import_into_edmv1_response_m_payload import DepositImportIntoEDMV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of DepositImportIntoEDMV1ResponseMPayload from a JSON string
deposit_import_into_edmv1_response_m_payload_instance = DepositImportIntoEDMV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(DepositImportIntoEDMV1ResponseMPayload.to_json())

# convert the object into a dict
deposit_import_into_edmv1_response_m_payload_dict = deposit_import_into_edmv1_response_m_payload_instance.to_dict()
# create an instance of DepositImportIntoEDMV1ResponseMPayload from a dict
deposit_import_into_edmv1_response_m_payload_from_dict = DepositImportIntoEDMV1ResponseMPayload.from_dict(deposit_import_into_edmv1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


