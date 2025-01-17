# BuyercontractGetCommunicationListV1Response

Response for GET /1/object/buyercontract/{pkiBuyercontractID}/getCommunicationList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m_payload** | [**BuyercontractGetCommunicationListV1ResponseMPayload**](BuyercontractGetCommunicationListV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.buyercontract_get_communication_list_v1_response import BuyercontractGetCommunicationListV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of BuyercontractGetCommunicationListV1Response from a JSON string
buyercontract_get_communication_list_v1_response_instance = BuyercontractGetCommunicationListV1Response.from_json(json)
# print the JSON string representation of the object
print(BuyercontractGetCommunicationListV1Response.to_json())

# convert the object into a dict
buyercontract_get_communication_list_v1_response_dict = buyercontract_get_communication_list_v1_response_instance.to_dict()
# create an instance of BuyercontractGetCommunicationListV1Response from a dict
buyercontract_get_communication_list_v1_response_from_dict = BuyercontractGetCommunicationListV1Response.from_dict(buyercontract_get_communication_list_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


