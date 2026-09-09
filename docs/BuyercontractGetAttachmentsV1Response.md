# BuyercontractGetAttachmentsV1Response

Response for GET /1/object/buyercontract/{pkiBuyercontractID}/getAttachments

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**BuyercontractGetAttachmentsV1ResponseMPayload**](BuyercontractGetAttachmentsV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.buyercontract_get_attachments_v1_response import BuyercontractGetAttachmentsV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of BuyercontractGetAttachmentsV1Response from a JSON string
buyercontract_get_attachments_v1_response_instance = BuyercontractGetAttachmentsV1Response.from_json(json)
# print the JSON string representation of the object
print(BuyercontractGetAttachmentsV1Response.to_json())

# convert the object into a dict
buyercontract_get_attachments_v1_response_dict = buyercontract_get_attachments_v1_response_instance.to_dict()
# create an instance of BuyercontractGetAttachmentsV1Response from a dict
buyercontract_get_attachments_v1_response_from_dict = BuyercontractGetAttachmentsV1Response.from_dict(buyercontract_get_attachments_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


