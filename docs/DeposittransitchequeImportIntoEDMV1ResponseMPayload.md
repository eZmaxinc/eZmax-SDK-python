# DeposittransitchequeImportIntoEDMV1ResponseMPayload

Payload for POST /1/object/deposittransitcheque/{pkiDeposittransitchequeID}/importIntoEDM

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_attachment** | [**List[CustomAttachmentImportIntoEDMResponse]**](CustomAttachmentImportIntoEDMResponse.md) |  | 

## Example

```python
from eZmaxApi.models.deposittransitcheque_import_into_edmv1_response_m_payload import DeposittransitchequeImportIntoEDMV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of DeposittransitchequeImportIntoEDMV1ResponseMPayload from a JSON string
deposittransitcheque_import_into_edmv1_response_m_payload_instance = DeposittransitchequeImportIntoEDMV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(DeposittransitchequeImportIntoEDMV1ResponseMPayload.to_json())

# convert the object into a dict
deposittransitcheque_import_into_edmv1_response_m_payload_dict = deposittransitcheque_import_into_edmv1_response_m_payload_instance.to_dict()
# create an instance of DeposittransitchequeImportIntoEDMV1ResponseMPayload from a dict
deposittransitcheque_import_into_edmv1_response_m_payload_from_dict = DeposittransitchequeImportIntoEDMV1ResponseMPayload.from_dict(deposittransitcheque_import_into_edmv1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


