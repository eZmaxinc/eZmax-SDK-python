# BuyercontractGetCommunicationCountV1ResponseMPayload

Response for GET /1/object/buyercontract/{pkiBuyercontractID}/getCommunicationCount

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**i_communication_count** | **int** | The count of Communication. | 

## Example

```python
from eZmaxApi.models.buyercontract_get_communication_count_v1_response_m_payload import BuyercontractGetCommunicationCountV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of BuyercontractGetCommunicationCountV1ResponseMPayload from a JSON string
buyercontract_get_communication_count_v1_response_m_payload_instance = BuyercontractGetCommunicationCountV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(BuyercontractGetCommunicationCountV1ResponseMPayload.to_json())

# convert the object into a dict
buyercontract_get_communication_count_v1_response_m_payload_dict = buyercontract_get_communication_count_v1_response_m_payload_instance.to_dict()
# create an instance of BuyercontractGetCommunicationCountV1ResponseMPayload from a dict
buyercontract_get_communication_count_v1_response_m_payload_from_dict = BuyercontractGetCommunicationCountV1ResponseMPayload.from_dict(buyercontract_get_communication_count_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


