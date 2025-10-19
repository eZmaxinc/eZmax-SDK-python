# BuyercontractImportIntoEDMV1ResponseMPayload

Payload for POST /1/object/buyercontract/{pkiBuyercontractID}/importIntoEDM

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_attachment** | [**List[CustomAttachmentImportIntoEDMResponse]**](CustomAttachmentImportIntoEDMResponse.md) |  | 

## Example

```python
from eZmaxApi.models.buyercontract_import_into_edmv1_response_m_payload import BuyercontractImportIntoEDMV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of BuyercontractImportIntoEDMV1ResponseMPayload from a JSON string
buyercontract_import_into_edmv1_response_m_payload_instance = BuyercontractImportIntoEDMV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(BuyercontractImportIntoEDMV1ResponseMPayload.to_json())

# convert the object into a dict
buyercontract_import_into_edmv1_response_m_payload_dict = buyercontract_import_into_edmv1_response_m_payload_instance.to_dict()
# create an instance of BuyercontractImportIntoEDMV1ResponseMPayload from a dict
buyercontract_import_into_edmv1_response_m_payload_from_dict = BuyercontractImportIntoEDMV1ResponseMPayload.from_dict(buyercontract_import_into_edmv1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


