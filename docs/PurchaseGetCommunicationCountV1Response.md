# PurchaseGetCommunicationCountV1Response

Response for GET /1/object/purchase/{pkiPurchaseID}/getCommunicationCount

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**PurchaseGetCommunicationCountV1ResponseMPayload**](PurchaseGetCommunicationCountV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.purchase_get_communication_count_v1_response import PurchaseGetCommunicationCountV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseGetCommunicationCountV1Response from a JSON string
purchase_get_communication_count_v1_response_instance = PurchaseGetCommunicationCountV1Response.from_json(json)
# print the JSON string representation of the object
print(PurchaseGetCommunicationCountV1Response.to_json())

# convert the object into a dict
purchase_get_communication_count_v1_response_dict = purchase_get_communication_count_v1_response_instance.to_dict()
# create an instance of PurchaseGetCommunicationCountV1Response from a dict
purchase_get_communication_count_v1_response_from_dict = PurchaseGetCommunicationCountV1Response.from_dict(purchase_get_communication_count_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


