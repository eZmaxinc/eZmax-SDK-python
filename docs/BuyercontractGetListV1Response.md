# BuyercontractGetListV1Response

Response for GET /1/object/buyercontract/getList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayloadGetList**](CommonResponseObjDebugPayloadGetList.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**BuyercontractGetListV1ResponseMPayload**](BuyercontractGetListV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.buyercontract_get_list_v1_response import BuyercontractGetListV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of BuyercontractGetListV1Response from a JSON string
buyercontract_get_list_v1_response_instance = BuyercontractGetListV1Response.from_json(json)
# print the JSON string representation of the object
print(BuyercontractGetListV1Response.to_json())

# convert the object into a dict
buyercontract_get_list_v1_response_dict = buyercontract_get_list_v1_response_instance.to_dict()
# create an instance of BuyercontractGetListV1Response from a dict
buyercontract_get_list_v1_response_from_dict = BuyercontractGetListV1Response.from_dict(buyercontract_get_list_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


