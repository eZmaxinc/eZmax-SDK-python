# BuyercontractGetCommunicationrecipientsV1Response

Response for GET /1/object/buyercontract/{pkiBuyercontractID}/getCommunicationrecipients

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**BuyercontractGetCommunicationrecipientsV1ResponseMPayload**](BuyercontractGetCommunicationrecipientsV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.buyercontract_get_communicationrecipients_v1_response import BuyercontractGetCommunicationrecipientsV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of BuyercontractGetCommunicationrecipientsV1Response from a JSON string
buyercontract_get_communicationrecipients_v1_response_instance = BuyercontractGetCommunicationrecipientsV1Response.from_json(json)
# print the JSON string representation of the object
print(BuyercontractGetCommunicationrecipientsV1Response.to_json())

# convert the object into a dict
buyercontract_get_communicationrecipients_v1_response_dict = buyercontract_get_communicationrecipients_v1_response_instance.to_dict()
# create an instance of BuyercontractGetCommunicationrecipientsV1Response from a dict
buyercontract_get_communicationrecipients_v1_response_from_dict = BuyercontractGetCommunicationrecipientsV1Response.from_dict(buyercontract_get_communicationrecipients_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


