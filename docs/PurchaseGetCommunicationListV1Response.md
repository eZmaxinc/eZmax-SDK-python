# PurchaseGetCommunicationListV1Response

Response for GET /1/object/purchase/{pkiPurchaseID}/getCommunicationList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayloadGetList**](CommonResponseObjDebugPayloadGetList.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**PurchaseGetCommunicationListV1ResponseMPayload**](PurchaseGetCommunicationListV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.purchase_get_communication_list_v1_response import PurchaseGetCommunicationListV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseGetCommunicationListV1Response from a JSON string
purchase_get_communication_list_v1_response_instance = PurchaseGetCommunicationListV1Response.from_json(json)
# print the JSON string representation of the object
print(PurchaseGetCommunicationListV1Response.to_json())

# convert the object into a dict
purchase_get_communication_list_v1_response_dict = purchase_get_communication_list_v1_response_instance.to_dict()
# create an instance of PurchaseGetCommunicationListV1Response from a dict
purchase_get_communication_list_v1_response_from_dict = PurchaseGetCommunicationListV1Response.from_dict(purchase_get_communication_list_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


