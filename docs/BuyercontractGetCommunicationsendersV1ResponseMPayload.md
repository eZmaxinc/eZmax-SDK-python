# BuyercontractGetCommunicationsendersV1ResponseMPayload

Response for GET /1/object/buyercontract/{pkiBuyercontractID}/getCommunicationsenders

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_communicationsenders** | [**List[CustomCommunicationsenderResponse]**](CustomCommunicationsenderResponse.md) |  | 

## Example

```python
from eZmaxApi.models.buyercontract_get_communicationsenders_v1_response_m_payload import BuyercontractGetCommunicationsendersV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of BuyercontractGetCommunicationsendersV1ResponseMPayload from a JSON string
buyercontract_get_communicationsenders_v1_response_m_payload_instance = BuyercontractGetCommunicationsendersV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(BuyercontractGetCommunicationsendersV1ResponseMPayload.to_json())

# convert the object into a dict
buyercontract_get_communicationsenders_v1_response_m_payload_dict = buyercontract_get_communicationsenders_v1_response_m_payload_instance.to_dict()
# create an instance of BuyercontractGetCommunicationsendersV1ResponseMPayload from a dict
buyercontract_get_communicationsenders_v1_response_m_payload_from_dict = BuyercontractGetCommunicationsendersV1ResponseMPayload.from_dict(buyercontract_get_communicationsenders_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


