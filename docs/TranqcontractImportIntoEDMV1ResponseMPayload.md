# TranqcontractImportIntoEDMV1ResponseMPayload

Payload for POST /1/object/tranqcontract/{pkiTranqcontractID}/importIntoEDM

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_attachment** | [**List[CustomAttachmentImportIntoEDMResponse]**](CustomAttachmentImportIntoEDMResponse.md) |  | 

## Example

```python
from eZmaxApi.models.tranqcontract_import_into_edmv1_response_m_payload import TranqcontractImportIntoEDMV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of TranqcontractImportIntoEDMV1ResponseMPayload from a JSON string
tranqcontract_import_into_edmv1_response_m_payload_instance = TranqcontractImportIntoEDMV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(TranqcontractImportIntoEDMV1ResponseMPayload.to_json())

# convert the object into a dict
tranqcontract_import_into_edmv1_response_m_payload_dict = tranqcontract_import_into_edmv1_response_m_payload_instance.to_dict()
# create an instance of TranqcontractImportIntoEDMV1ResponseMPayload from a dict
tranqcontract_import_into_edmv1_response_m_payload_from_dict = TranqcontractImportIntoEDMV1ResponseMPayload.from_dict(tranqcontract_import_into_edmv1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


