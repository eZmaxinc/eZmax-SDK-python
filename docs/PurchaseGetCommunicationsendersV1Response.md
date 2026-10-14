# PurchaseGetCommunicationsendersV1Response

Response for GET /1/object/purchase/{pkiPurchaseID}/getCommunicationrecipients

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**PurchaseGetCommunicationsendersV1ResponseMPayload**](PurchaseGetCommunicationsendersV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.purchase_get_communicationsenders_v1_response import PurchaseGetCommunicationsendersV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseGetCommunicationsendersV1Response from a JSON string
purchase_get_communicationsenders_v1_response_instance = PurchaseGetCommunicationsendersV1Response.from_json(json)
# print the JSON string representation of the object
print(PurchaseGetCommunicationsendersV1Response.to_json())

# convert the object into a dict
purchase_get_communicationsenders_v1_response_dict = purchase_get_communicationsenders_v1_response_instance.to_dict()
# create an instance of PurchaseGetCommunicationsendersV1Response from a dict
purchase_get_communicationsenders_v1_response_from_dict = PurchaseGetCommunicationsendersV1Response.from_dict(purchase_get_communicationsenders_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


