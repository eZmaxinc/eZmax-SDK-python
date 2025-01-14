# BuyercontractGetCommunicationsendersV1Response

Response for GET /1/object/buyercontract/{pkiBuyercontractID}/getCommunicationrecipients

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**BuyercontractGetCommunicationsendersV1ResponseMPayload**](BuyercontractGetCommunicationsendersV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.buyercontract_get_communicationsenders_v1_response import BuyercontractGetCommunicationsendersV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of BuyercontractGetCommunicationsendersV1Response from a JSON string
buyercontract_get_communicationsenders_v1_response_instance = BuyercontractGetCommunicationsendersV1Response.from_json(json)
# print the JSON string representation of the object
print(BuyercontractGetCommunicationsendersV1Response.to_json())

# convert the object into a dict
buyercontract_get_communicationsenders_v1_response_dict = buyercontract_get_communicationsenders_v1_response_instance.to_dict()
# create an instance of BuyercontractGetCommunicationsendersV1Response from a dict
buyercontract_get_communicationsenders_v1_response_from_dict = BuyercontractGetCommunicationsendersV1Response.from_dict(buyercontract_get_communicationsenders_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


