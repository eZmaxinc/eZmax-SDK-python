# BuyercontractGetCommunicationrecipientsV1ResponseMPayload

Response for GET /1/object/buyercontract/{pkiBuyercontractID}/getCommunicationrecipients

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_communicationrecipientsgroup** | [**List[CustomCommunicationrecipientsgroupResponse]**](CustomCommunicationrecipientsgroupResponse.md) |  | 

## Example

```python
from eZmaxApi.models.buyercontract_get_communicationrecipients_v1_response_m_payload import BuyercontractGetCommunicationrecipientsV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of BuyercontractGetCommunicationrecipientsV1ResponseMPayload from a JSON string
buyercontract_get_communicationrecipients_v1_response_m_payload_instance = BuyercontractGetCommunicationrecipientsV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(BuyercontractGetCommunicationrecipientsV1ResponseMPayload.to_json())

# convert the object into a dict
buyercontract_get_communicationrecipients_v1_response_m_payload_dict = buyercontract_get_communicationrecipients_v1_response_m_payload_instance.to_dict()
# create an instance of BuyercontractGetCommunicationrecipientsV1ResponseMPayload from a dict
buyercontract_get_communicationrecipients_v1_response_m_payload_from_dict = BuyercontractGetCommunicationrecipientsV1ResponseMPayload.from_dict(buyercontract_get_communicationrecipients_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


