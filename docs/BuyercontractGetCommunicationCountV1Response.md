# BuyercontractGetCommunicationCountV1Response

Response for GET /1/object/buyercontract/{pkiBuyercontractID}/getCommunicationCount

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m_payload** | [**BuyercontractGetCommunicationCountV1ResponseMPayload**](BuyercontractGetCommunicationCountV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.buyercontract_get_communication_count_v1_response import BuyercontractGetCommunicationCountV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of BuyercontractGetCommunicationCountV1Response from a JSON string
buyercontract_get_communication_count_v1_response_instance = BuyercontractGetCommunicationCountV1Response.from_json(json)
# print the JSON string representation of the object
print(BuyercontractGetCommunicationCountV1Response.to_json())

# convert the object into a dict
buyercontract_get_communication_count_v1_response_dict = buyercontract_get_communication_count_v1_response_instance.to_dict()
# create an instance of BuyercontractGetCommunicationCountV1Response from a dict
buyercontract_get_communication_count_v1_response_from_dict = BuyercontractGetCommunicationCountV1Response.from_dict(buyercontract_get_communication_count_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


